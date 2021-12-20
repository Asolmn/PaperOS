from flask import request, jsonify
from werkzeug.utils import secure_filename
from app.paper import paper
from app.models import Role, User, Student, Teacher, \
    Topic, Paper, change_msg
import uuid
import os

UPLOAD_FOLDER = '.../uploads/'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc'}


# 判断是否在允许扩展名之内
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@paper.route('/receivefile', methods=['POST'])
def receive_file():
    if request.method == 'POST':
        # data = request.form.get('username')
        # 检查post请求是否包含文件部分
        if 'file' not in request.files:
            return jsonify({'msg': "No file part"})

        file = request.files['file']
        if file.filename == '':
            return jsonify({'msg': "No selected file"})

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            uuids = str(uuid.uuid3(uuid.NAMESPACE_DNS, filename))
            file.save(os.path.join(UPLOAD_FOLDER), uuids)
            temp = Paper.query.filter_by(uuid=uuids).first()
            if temp is None:
                paper = Paper(
                    filename=filename,
                    uuid=uuids
                )
                paper.save_db()
            return jsonify(change_msg(paper.to_json()))
    return jsonify({'msg': 'fail'})