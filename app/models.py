from app import db


def change_msg(res):
    res['msg'] = "success"
    res['flag'] = 1
    return res


class User(db.Model):
    """管理员"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True) # 用户名
    password = db.Column(db.String(64)) # 密码
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # 所属角色

    # 返回序列化
    def to_json(self):
        result = {
            'userinfo': [
                {
                    'id': self.id,
                    'username': self.username,
                    'password': self.password,
                    'role': self.admin.name
                }
            ],
            'msg': "",
            'flag': 0
        }
        return result

    def save_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return self.username


class Teacher(db.Model):
    """教师"""
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64)) # 教师名
    password = db.Column(db.String(64)) # 密码
    students = db.relationship('Student', backref='teac', lazy='dynamic') # 指导的学生
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # 属实角色

    def to_json(self):
        # 获取当前的学生列表
        studentlist = []
        for i in self.students.all():
            studentlist.append(str(i))
        result = {
            'teacherinfo': [
                {
                    'id': self.id,
                    'username': self.username,
                    'password': self.password,
                    'students': studentlist
                }
            ],
            'msg': "",
            'flag': 0
        }
        return result

    def save_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return self.username


class Student(db.Model):
    """学生"""
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64)) # 学生名
    password = db.Column(db.String(64)) # 密码
    topics = db.relationship('Topic', backref='stu', lazy='dynamic') # 课题
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # 角色
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id')) # 所属教师

    # 序列化
    def to_json(self):
        # 获取学生课题列表
        topiclist = []
        for i in self.topics.all():
            topiclist.append(str(i))
        # 响应信息
        result = {
            'studentinfo': [
                {
                    'id': self.id,
                    'username': self.username,
                    'password': self.password,
                    'teacher': self.teacher_id,
                    'topics': topiclist
                }
            ],
            'msg': "",
            'flag': 0
        }
        return result

    # 修改或者添加到数据库
    def save_db(self):
        db.session.add(self)
        db.session.commit()

    # 从数据库中删除
    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return self.username


class Topic(db.Model):
    """课题"""
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    topicname = db.Column(db.String(128), unique=True, nullable=False) # 课题名词
    uuid = db.Column(db.Integer, unique=True) # 课题唯一UUID
    student_id = db.Column(db.Integer, db.ForeignKey('students.id')) # 课题所属学生
    status = db.Column(db.Boolean, default=False) # 课题通过状态

    def __repr__(self):
        return self.uuid


class Role(db.Model):
    """角色"""
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True) # 角色名
    default = db.Column(db.Boolean, default=False, index=True) # 默认角色
    permissions = db.Column(db.Integer) # 权限
    # users = db.relationship('User', backref='role', lazy='dynamic')
    # 所属管理员的用户
    users = db.relationship(
        'User',
        foreign_keys = [User.role_id],
        backref = db.backref('admin', lazy='joined'),
        lazy = 'dynamic',
        cascade = 'all, delete-orphan'
    )
    # 所属教师的用户
    teachers = db.relationship(
        'Teacher',
        foreign_keys = [Teacher.role_id],
        backref = db.backref('teacher', lazy='joined'),
        lazy='dynamic',
        cascade = 'all, delete-orphan'
    )
    # 所属学生的用户
    students = db.relationship(
        'Student',
        foreign_keys = [Student.role_id],
        backref = db.backref('student', lazy='joined'),
        lazy='dynamic',
        cascade = 'all, delete-orphan'
    )

    # 返回序列化
    def to_json(self):
        users = []
        teachers = []
        students = []
        # 获取当前角色下的所有用户
        for user in self.users.all():
            users.append(str(user))

        for teacher in self.teachers.all():
            teachers.append(str(teacher))

        for student in self.students.all():
            students.append(str(student))
        # 响应信息
        result = {
            'roleinfo': [
                {
                    'id': self.id,
                    'name': self.name,
                    'permissions': self.permissions,
                    'users': users,
                    'teacher': teachers,
                    'student': students
                }
            ],
            'msg': "",
            'flag': 0
        }
        return result

    def save_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return self.name
