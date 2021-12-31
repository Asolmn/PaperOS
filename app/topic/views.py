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
    return jsonify({'msg': 'fail', 'flag': 0})


# 删除课题
@topic.route('/deletetopic', methods=['DELETE'])
def delete_topic():
    data = request.get_json()
    print(data)
    uuids = data['uuids']
    # 根据uuid查询对应的课题
    temp = Topic.query.filter_by(uuid=uuids).first()
    if temp is not None:
        # 获取课题数据
        res = change_msg(temp.to_json())
        temp.delete_db() # 删除课题
        return jsonify(res)
    return jsonify({'msg': 'fail', 'flag': 0})


@topic.route('/changetopicname', methods=['PUT'])
def change_topicname():
    data = request.get_json()
    uuids = data['uuids']
    topicname = data['topicname']
    temp = Topic.query.filter_by(uuid=uuids).first()
    if temp is not None:
        temp.topicname = topicname
        temp.save_db()
        return jsonify(change_msg(temp.to_json()))
    return jsonify({'msg': 'fail', 'flag': 0})

# 修改课题状态
@topic.route('/truestatus', methods=['PUT'])
def true_status():
    data = request.get_json() # 获取数据
    uuids = data['uuids'] # 获取uuid
    temp = Topic.query.filter_by(uuid=uuids).first() # 查询对象
    if temp is not None:
        temp.status = True # 修改状态
        temp.save_db() # 重新提交数据库
        res = change_msg(temp.to_json()) # 返回数据
        return jsonify(res)
    return jsonify({'msg': 'fail', 'flag': 0})


# 修改课题状态
@topic.route('/falsestatus', methods=['PUT'])
def false_status():
    data = request.get_json()
    uuids = data['uuids']
    temp = Topic.query.filter_by(uuid=uuids).first()
    if temp is not None:
        temp.status = False
        temp.save_db()
        res = change_msg(temp.to_json())
        return jsonify(res)
    return jsonify({'msg': 'fail', 'flag': 0})


#获取课题信息
@topic.route('/gettopicinfo', methods=['POST'])
def get_info():
    data = request.get_json()
    uuids = data['uuids']
    temp = Topic.query.filter_by(uuid=uuids).first()
    if temp is not None:
        return jsonify(change_msg(temp.to_json()))
    return jsonify({'msg': 'fail', 'flag': 0})


# 获取当前学生所有课题
@topic.route('/stutopic', methods=['POST'])
def get_stu_topic():
    data = request.get_json()
    id = data['id']
    student = Student.query.filter_by(id=id).first()
    topiclist = student.to_json()['studentinfo'][0]['topics']
    print(topiclist)
    topicinfo = []
    if student is not None:
        for i in topiclist:
            temp = Topic.query.filter_by(uuid=i).first()
            # topicinfo.append(change_topic_flag(temp.topic_json())[0])
            res = temp.to_json()['topicinfo'][0]
            res['msg'] = "success"
            res['flag'] = 1
            topicinfo.append(res)
        return jsonify(topicinfo)
    return jsonify({'msg': 'fail', 'flag': 0})


# 获取所指导学生的所有课题
@topic.route('/alltopic', methods=['POST'])
def all_topic():
    data = request.get_json()
    id = data['id']
    teacher = Teacher.query.filter_by(id=id).first()
    studentlist = teacher.to_json()['teacherinfo'][0]['students']
    topiclist = []
    topicinfo = []
    if teacher is not None:
        for i in studentlist:
            temp = Student.query.filter_by(username=i).first()
            topiclist += temp.to_json()['studentinfo'][0]['topics']
        for j in topiclist:
            topic = Topic.query.filter_by(uuid=j).first()
            res = topic.to_json()['topicinfo'][0]
            res['msg'] = "success"
            res['flag'] = 1
            topicinfo.append(res)
        return jsonify(topicinfo)
    return jsonify({'msg': 'fail', 'flag': 0})





