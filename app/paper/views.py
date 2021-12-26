from flask import request, jsonify, send_from_directory, send_file
from werkzeug.utils import secure_filename
from app.paper import paper
from app.models import Role, User, Student, Teacher, \
    Topic, Paper, change_msg
import uuid
import os

UPLOAD_FOLDER = 'D:/Project/PaperOS/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc'}


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
            filename = secure_filename(file.filename) # 获取文件名
            print(filename)
            suffix = get_suffix(file.filename) # 获取文件后缀
            uuids = str(uuid.uuid4()) # 对文件名进行uuids重命名

            name = uuids+"."+suffix # 文件保存名

            path = os.path.join(UPLOAD_FOLDER, name) # 保存路径
            file.save(path) # 保存文件

            temp = Paper.query.filter_by(uuid=uuids).first() # 查询是否已经存在该文件
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
    uuid = data['uuid'] # 获取文件uuid
    filedata = Paper.query.filter_by(uuid=uuid).first() # 获取文件数据
    path = filedata.path # 文件路径
    return send_file(path)