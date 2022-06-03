from flask import request, jsonify
from app.auth import auth
from app.models import Role, User, Student, Teacher, change_msg


@auth.route('/helloworld', methods=['GET', 'POST'])
def hellworld():
    return jsonify({'msg': 'helloworld'})


# 登录用户
@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.get_json(silent=True)
    print(data)
    username = data['username']
    password = data['password']
    role = data['role']
    # 判断不同角色，获取查询不同的表
    if role == 'Admin':
        user = User.query.filter_by(username=username).first()
        # 如果用户存在且密码验证通过
        if user is not None and user.password == password:
            # 返回用户信息
            return jsonify(change_msg(user.to_json()))
    if role == 'Student':
        student = Student.query.filter_by(username=username).first()
        if student is not None and student.password == password:
            return jsonify(change_msg(student.to_json()))
    if role == 'Teacher':
        teacher = Teacher.query.filter_by(username=username).first()
        if teacher is not None and teacher.password == password:
            return jsonify(change_msg(teacher.to_json()))
    return jsonify({'msg': 'fail', 'flag': 0})

# 注册用户
@auth.route('/register', methods=['GET', 'POST'])
def register():
    # 获取post提交的数据
    data = request.get_json()
    username = data['username']
    password = data['password']
    # teac = data['teac']
    role = data['role']
    # 获取角色
    roles = Role.query.filter_by(name=role).first()
    # teacher = Teacher.query.filter_by(username=teac).first()
    if role == 'Admin':
        # 获取用户的角色
        temp = User.query.filter_by(username=username).first()
        if temp is None:
            # 如果用户不存在，则添加用户，提交到数据库中
            # admin指定管理员角色
            user = User(
                username=username,
                password=password,
                admin=roles)
            user.save_db()  # 提交用户
            res = change_msg(user.to_json())  # 返回响应
            return jsonify(res)
    if role == 'Student':
        temp = Student.query.filter_by(username=username).first()
        if temp is None:
            # student指定学生角色, teac指定教师
            student = Student(
                username=username,
                password=password,
                student=roles)
                # teac=teacher)
            student.save_db()
            res = change_msg(student.to_json())
            return jsonify(res)
    if role == 'Teacher':
        temp = Teacher.query.filter_by(username=username).first()
        if temp is None:
            # teacher指定教师角色
            teacher = Teacher(
                username=username,
                password=password,
                teacher=roles)
            teacher.save_db()
            res = change_msg(teacher.to_json())
            return jsonify(res)
    return jsonify({'msg': 'fail', 'flag': 0})


# 返回指定用户的信息
@auth.route('/getuser', methods=['GET', 'POST'])
def get_user():
    # 获取post信息
    data = request.get_json()
    username = data['username']
    role = data['role']

    # 根据不同的角色，查询不同的表
    if role == 'Admin':
        # 查询用户
        user = User.query.filter_by(username=username).first()
        # 如果用户不为空
        if user is not None:
            # 返回信息
            return jsonify(change_msg(user.to_json()))
    if role == 'Student':
        student = Student.query.filter_by(username=username).first()
        if student is not None:
            return jsonify(change_msg(student.to_json()))
    if role == 'Teacher':
        teacher = Teacher.query.filter_by(username=username).first()
        if teacher is not None:
            return jsonify(change_msg(teacher.to_json()))
    return jsonify({'msg': 'fail', 'flag': 0})

# 返回指定用户的信息
@auth.route('/getuserid', methods=['GET', 'POST'])
def get_user_id():
    # 获取post信息
    data = request.get_json()
    id = data['id']
    role = data['role']

    # 根据不同的角色，查询不同的表
    if role == 'Admin':
        # 查询用户
        user = User.query.filter_by(id=id).first()
        # 如果用户不为空
        if user is not None:
            # 返回信息
            return jsonify(change_msg(user.to_json()))
    if role == 'Student':
        student = Student.query.filter_by(id=id).first()
        if student is not None:
            return jsonify(change_msg(student.to_json()))
    if role == 'Teacher':
        teacher = Teacher.query.filter_by(id=id).first()
        if teacher is not None:
            return jsonify(change_msg(teacher.to_json()))
    return jsonify({'msg': 'fail', 'flag': 0})



# 返回指定角色的用户信息
@auth.route('/userinfo', methods=['GET', 'POST'])
def user_info():
    data = request.get_json()
    role = data['role']
    roles = Role.query.filter_by(name=role).first()
    infolist = []
    if role == 'Admin':
        # 获取当前角色下面的所有用户
        users = User.query.filter_by(admin=roles).all()
        # 循环将用户加入到列表中
        for i in users:
            res = i.to_json()['userinfo'][0]
            res['msg'] = "success"
            res['flag'] = 1
            infolist.append(res)
        return jsonify(infolist)
    if role == 'Student':
        students = Student.query.filter_by(student=roles).all()
        for i in students:
            res = i.to_json()['studentinfo'][0]
            res['msg'] = "success"
            res['flag'] = 1
            infolist.append(res)
        return jsonify(infolist)
    if role == 'Teacher':
        teachers = Teacher.query.filter_by(teacher=roles).all()
        for i in teachers:
            res = i.to_json()['teacherinfo'][0]
            res['msg'] = "success"
            res['flag'] = 1
            infolist.append(res)
        return jsonify(infolist)
    return jsonify({'msg': 'fail', 'flag': 0})


# 获取所有用户信息
@auth.route('/alluser', methods=['GET', 'POST'])
def all_user():
    # 查询三个表的所有信息
    users = User.query.all()
    student = Student.query.all()
    teacher = Teacher.query.all()
    # 依次添加到列表中
    infolist = []
    for i in users:
        infolist.append(i.to_json())
    for i in student:
        infolist.append(i.to_json())
    for i in teacher:
        infolist.append(i.to_json())
    res = {'info': infolist}
    return jsonify(res)


# 创建角色
@auth.route('/createrole', methods=['GET', 'POST'])
def create_role():
    # 获取post信息，传入角色名和权限值
    data = request.get_json()
    name = data['role']
    permissions = data['permissions']
    temp = Role.query.filter_by(name=name).first()
    # 如果不存在当前角色，则进行创建
    if temp is None:
        role = Role(
            name=name,
            permissions=permissions
        )
        role.save_db()
        return jsonify(role.to_json())
    return jsonify({'msg': 'fail', 'flag': 0})


# 返回指定角色的信息
@auth.route('/getrole', methods=['GET', 'POST'])
def get_role():
    # 获取post信息，传入角色名
    name = request.json.get('role')
    role = Role.query.filter_by(name=name).first()
    # 如果角色存在
    if role is not None:
        res = role.to_json()
        return jsonify(res)
    return jsonify({'msg': 'fail', 'flag': 0})


# 获取所有角色信息
@auth.route('/allrole', methods=['GET', 'POST'])
def all_role():
    # 获取所有角色
    roles = Role.query.all()
    # 创建角色信息列表
    rolelist = []
    for i in roles:
        rolelist.append(i.to_json())
    res = {'info': rolelist}
    return jsonify(res)


# 删除角色
@auth.route('/deletrole', methods=['DELETE'])
def delete_role():
    data = request.get_json()
    name = data['name']
    role = Role.query.filter_by(name=name).first()
    if role is not None:
        res = change_msg(role.to_json())
        role.delete_db()
        return jsonify(res)
    return jsonify({'msg': 'fail', 'flag': 0})

# 删除用户
@auth.route('/deleteuser', methods=['DELETE'])
def delete_user():
    #获取post信息，传入用户id和角色
    data = request.get_json()
    id = data['id']
    role = data['role']
    if role == 'Admin':
        user = User.query.filter_by(id=id).first()
        res = change_msg(user.to_json())
        user.delete_db()
        return jsonify(res)
    if role == 'Student':
        student = Student.query.filter_by(id=id).first()
        res = change_msg(student.to_json())
        student.delete_db()
        return jsonify(res)
    if role == 'Teacher':
        teacher = Teacher.query.filter_by(id=id).first()
        res = change_msg(teacher.to_json())
        teacher.delete_db()
        return jsonify(res)
    return jsonify({'msg': 'fail', 'flag': 0})


# 更新用户名
@auth.route('/updateuserinfo', methods=['PUT'])
def update_user():
    data = request.get_json()
    role = data['role']
    id = data['id']
    if role == 'Admin':
        user = User.query.filter_by(id=id).first()
        user.username = data['username']
        user.save_db()
        return jsonify(change_msg(user.to_json()))
    if role == 'Student':
        user = Student.query.filter_by(id=id).first()
        user.username = data['username']
        user.save_db()
        return jsonify(change_msg(user.to_json()))
    if role == 'Teacher':
        user = Teacher.query.filter_by(id=id).first()
        user.username = data['username']
        user.save_db()
        return jsonify(change_msg(user.to_json()))
    return jsonify({'msg': 'fail', 'flag': 0})


# 指定教师
@auth.route('/selectteacher', methods=['PUT'])
def selectteacher():
    data = request.get_json()
    stuid = data['stuid'] # 学生id
    teaname = data['teaname'] # 教师姓名
    student = Student.query.filter_by(id=stuid).first() # 学生数据对象
    teacher = Teacher.query.filter_by(username=teaname).first() # 教师数据对象
    if student is not None and teacher is not None:
        student.teac = teacher
        student.save_db()
        return jsonify(change_msg(student.to_json()))
    return jsonify({'msg': 'fail', 'flag': 0})


# 修改用户角色
@auth.route('/updateuserrole', methods=['PUT'])
def update_user_role():
    data = request.get_json()
    id = data['id']
    role = data['role']
    updaterole = data['updaterole']
    # roles = Role.query.filter_by(name=role).first()
    updateroles = Role.query.filter_by(name=updaterole).first()
    if role == 'Admin':
        user = User.query.filter_by(id=id).first()
        user.admin = updateroles
        user.save_db();
        return jsonify(change_msg(user.to_json()))
    if role == 'Student':
        user = Student.query.filter_by(id=id).first()
        user.student = updateroles
        user.save_db();
        return jsonify(change_msg(user.to_json()))
    if role == 'Teacher':
        user = Teacher.query.filter_by(id=id).first()
        user.student = updateroles
        user.save_db();
        return jsonify(change_msg(user.to_json()))
    return jsonify({'msg': 'fail', 'flag': 0})

# 获取当前教师的所有学生列表
@auth.route('/teastulist', methods=['POST'])
def get_tea_stulist():
    data = request.get_json()
    id = data['id']
    teacher = Teacher.query.filter_by(id=id).first()
    stulist = teacher.to_json()['teacherinfo'][0]['students'] # 学生列表
    stulistinfo = [] # 返回学生信息
    print(stulist)
    # 教师不为0
    if teacher is not None:
        for i in stulist:
            # 查询每一个对应的学生对象
            temp = Student.query.filter_by(username=i).first()
            res = temp.to_json()['studentinfo'][0]
            res['msg'] = "success"
            res['flag'] = 1
            stulistinfo.append(res)
        return jsonify(stulistinfo)
    return jsonify({'msg': 'fail', 'flag': 0})


# 解除用户与指导老师之间的关系
@auth.route('/relievestu', methods=['PUT'])
def relieve_stu():
    data = request.get_json()
    stuid = data['stuid']
    # teaid = data['teaid']
    student = Student.query.filter_by(id=stuid).first()
    if student is not None:
        student.teac = None
        student.teacher_id = None
        student.save_db()
        return jsonify(change_msg(student.to_json()))
    return jsonify({'msg': 'fail', 'flag': 0})


# 获取教师所属的学生列表,只包含用户名和id
@auth.route('/allstulist', methods=['POST'])
def all_stu_list():
    data = request.get_json()
    id = data['id']
    infolist = []
    stuinfo = {}
    teacher = Teacher.query.filter_by(id=id).first()
    stulist = teacher.to_json()['teacherinfo'][0]['students'] # 学生列表
    if teacher is not None:
        for i in stulist:
            # 查询每一个对应的学生对象
            temp = Student.query.filter_by(username=i).first()
            infolist.append({'username': temp.to_json()['studentinfo'][0]['username'], 'stuid':temp.to_json()['studentinfo'][0]['id']})
        return jsonify(infolist)
    return jsonify({'msg': 'fail', 'flag': 0})



