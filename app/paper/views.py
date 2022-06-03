from flask import request, jsonify, send_from_directory, send_file
from werkzeug.utils import secure_filename

import app
from app.paper import paper
from app.models import Role, User, Student, Teacher, \
    Topic, Paper, change_msg
import uuid
import os

# UPLOAD_FOLDER = os.path.abspath(os.path.join(os.getcwd(), r"../../uploads"))
UPLOAD_FOLDER="/root/project/PaperOS/uploads"
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc'}

# print(os.path.abspath(os.path.join(os.getcwd(), r"../../uploads"))
# 判断是否在允许扩展名之内
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 获取文件名（无后缀）
def split_file(filename):
    return filename.rsplit('.', 1)[0].lower()


# 获取后缀
def get_suffix(filename):
    return filename.rsplit('.', 1)[1].lower()


@paper.route('/receivefile', methods=['POST'])
def receive_file():
    if request.method == 'POST':
        id = request.form.get('id')
        student = Student.query.filter_by(id=id).first()
        # 检查post请求是否包含文件部分
        if 'file' not in request.files:
            return jsonify({'msg': "No file part"})

        # 检查是否为空文件
        file = request.files['file']
        if file.filename == '':
            return jsonify({'msg': "No selected file"})

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # 获取文件名
            print(filename)
            suffix = get_suffix(file.filename)  # 获取文件后缀
            uuids = str(uuid.uuid4())  # 对文件名进行uuids重命名

            name = uuids + "." + suffix  # 文件保存名

            path = os.path.join(UPLOAD_FOLDER, name)  # 保存路径
            print(path)
            file.save(path)  # 保存文件

            temp = Paper.query.filter_by(uuid=uuids).first()  # 查询是否已经存在该文件
            # 如果文件不存在，则创建对应的文件记录
            if temp is None and Student is not None:
                paper = Paper(
                    filename=filename,
                    uuid=uuids,
                    path=path,
                    stupaper=student
                )
                paper.save_db()
                return jsonify(change_msg(paper.to_json()))
    return jsonify({'msg': 'fail'})


# 下载文件
@paper.route('/downloadfile', methods=['POST'])
def download_file():
    data = request.get_json()
    uuid = data['uuid']  # 获取文件uuid
    filedata = Paper.query.filter_by(uuid=uuid).first()  # 获取文件数据
    path = filedata.path  # 文件路径
    print(type(send_file(path)))
    return send_file(path)


# 查询论文文件信息
@paper.route('/selectinfo', methods=['POST'])
def select_info():
    data = request.get_json()
    uuid = data['uuid']
    paper = Paper.query.filter_by(uuid=uuid).first()
    if paper is not None:
        return jsonify(change_msg(paper.to_json()))
    return jsonify({'msg': 'fail'})


# 获取学生的所有论文文件信息
@paper.route('/stupaperinfo', methods=['POST'])
def stu_paper():
    data = request.get_json()
    id = data['id']
    student = Student.query.filter_by(id=id).first()
    paperinfo = student.to_json()['studentinfo'][0]['papers']
    paperlist = []
    for i in paperinfo:
        paper = Paper.query.filter_by(uuid=i).first()
        paperlist.append(change_msg(paper.to_json())['paperinfo'][0])
    return jsonify({'info': paperlist})


# 获取所指导学生的所有论文文件信息
@paper.route('/allstupaper', methods=['POST'])
def all_stu_paper():
    data = request.get_json()
    id = data['id']
    teacher = Teacher.query.filter_by(id=id).first()
    studentlist = teacher.to_json()['teacherinfo'][0]['students']
    paperlist = [] # 论文列表
    paperinfo = [] # 论文信息
    if teacher is not None:
        for i in studentlist:
            temp = Student.query.filter_by(username=i).first()
            paperlist += temp.to_json()['studentinfo'][0]['papers']
        for j in paperlist:
            paper = Paper.query.filter_by(uuid=j).first()
            res = paper.to_json()['paperinfo'][0]
            res['msg'] = "success"
            res['flag'] = 1
            paperinfo.append(res)
        return jsonify(paperinfo)
    return jsonify({'msg': 'fail', 'flag': 0})


# 修改论文状态为通过
@paper.route('/truepaper', methods=['PUT'])
def true_paper():
    data = request.get_json()
    uuid = data['uuid']
    temp = Paper.query.filter_by(uuid=uuid).first()
    if temp is not None:
        temp.status = True
        temp.save_db()
        res = change_msg(temp.to_json())  # 返回数据
        return jsonify(res)
    return jsonify({'msg': 'fail', 'flag': 0})


# 修改论文状态为不通过
@paper.route('/falsepaper', methods=['PUT'])
def false_paper():
    data = request.get_json()
    uuid = data['uuid']
    temp = Paper.query.filter_by(uuid=uuid).first()
    if temp is not None:
        temp.status = False
        temp.save_db()
        res = change_msg(temp.to_json())  # 返回数据
        return jsonify(res)
    return jsonify({'msg': 'fail', 'flag': 0})

