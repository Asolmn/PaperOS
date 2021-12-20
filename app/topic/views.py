from flask import request, jsonify
from app.topic import topic
from app.models import Role, User, Student, Teacher, Topic, change_msg
import uuid

# 创建课题
@topic.route('/createtopic', methods=['POST'])
def create_topic():
    data = request.get_json()
    topicname = data['topicname']
    # 创建课题的学生
    username = data['username']
    # 根据课题名生成uuid
    uuids = str(uuid.uuid3(uuid.NAMESPACE_DNS, topicname))
    print(uuid)
    temp = Topic.query.filter_by(uuid=uuid).first()
    if temp is None:
        student = Student.query.filter_by(username=username).first()
        topic = Topic(
            topicname=topicname,
            uuid=uuids,
            stutopic=student
        )
        topic.save_db()
        return jsonify(change_msg(topic.to_json()))
    return jsonify({'msg': 'fail'})


# 删除课题
@topic.route('/deletetopic', methods=['DELETE'])
def delete_topic():
    data = request.get_json()
    uuids = data['uuids']
    # 根据uuid查询对应的课题
    temp = Topic.query.filter_by(uuid=uuids).first()
    if temp is not None:
        # 获取课题数据
        res = change_msg(temp.to_json())
        temp.delete_db() # 删除课题
        return jsonify(res)
    return jsonify({'msg': 'fail'})


# 修改课题状态
@topic.route('/changestatus', methods=['PUT'])
def change_status():
    data = request.get_json()
    uuids = data['uuids']
    temp = Topic.query.filter_by(uuid=uuids).first()
    if temp is not None:
        temp.status = True
        temp.save_db()
        res = change_msg(temp.to_json())
        return jsonify(res)
    return jsonify({'msg': 'fail'})



