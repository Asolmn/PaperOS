from flask import request, jsonify
from app.topic import topic
from app.models import Role, User, Student, Teacher, Topic, change_msg
import uuid


@topic.route('/createtopic', methods=['POST'])
def create_topic():
    data = request.get_json()
    topicname = data['topicname']
    username = data['username']
    uuids = str(uuid.uuid3(uuid.NAMESPACE_DNS, topicname))
    print(uuid)
    temp = Topic.query.filter_by(uuid=uuid).first()
    if temp is None:
        student = Student.query.filter_by(username=username).first()
        topic = Topic(
            topicname=topicname,
            uuid=uuids,
            stu=student
        )
        topic.save_db()
        return jsonify(change_msg(topic.to_json()))
    return jsonify({'msg': 'fail'})


@topic.route('/deletetopic', methods=['DELETE'])
def delete_topic():
    data = request.get_json()
    uuids = data['uuids']


