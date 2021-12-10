from flask import request, jsonify
from app.auth import auth
from app.models import Role, User


@auth.route('/helloworld', methods=['GET', 'POST'])
def hellworld():
    return jsonify({'msg': 'helloworld'})


# 登录用户
@auth.route('/login', methods=['GET', 'POST'])
def login():
    name = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=name).first()
    if user is not None and user.password == password:
        res = user.to_json()
        res['msg'] = "success"
        res['flag'] = 1
        return jsonify(res)
    return jsonify({'msg': "fail"})


# 注册用户
@auth.route('/register', methods=['GET', 'POST'])
def register():
    # 获取post提交的数据
    name = request.json.get('username')
    password = request.json.get('password')
    role = request.json.get('role')

    # 获取用户的角色
    roles = Role.query.filter_by(name=role).first()
    temp = User.query.filter_by(username=name).first()
    if temp is None:
        # 如果用户不存在，则添加用户，提交到数据库中
        user = User(
            username=name,
            password=password,
            role=roles
        )
        # 提交用户
        user.save_db()
        # 返回响应
        res = user.to_json()
        print(res)
        res['msg'] = "success"
        res['flag'] = 1

        return jsonify(res)
    return jsonify({'msg': "fail"})

# 返回指定用户的信息
@auth.route('/getuser', methods=['GET', 'POST'])
def getuser():
    name = request.json.get('username')
    user = User.query.filter_by(username=name).first()
    if user is not None:
        res = user.to_json()
        res['msg'] = "success"
        res['flag'] = 1
        return jsonify(res)
    return jsonify({'msg': "fail"})


# 返回指定角色的信息
@auth.route('/getrole', methods=['GET', 'POST'])
def getrole():
    name = request.json.get('name')
    role = Role.query.filter_by(name=name).first()
    if role is not None:

        res = role.to_json()
        return jsonify(res)
    return jsonify({'msg': "fail"})


# 获取所有用户信息
@auth.route('/alluser', methods=['GET', 'POST'])
def alluser():
    users = User.query.all()
    userlist = []
    for i in users:
        userlist.append(i.to_json())
    res = {'info': userlist}
    return jsonify(res)


# 获取所有角色信息
@auth.route('/allrole', methods=['GET', 'POST'])
def allrole():
    roles = Role.query.all()
    rolelist = []
    for i in roles:
        rolelist.append(i.to_json())
    res = {'info': rolelist}
    return jsonify(res)
