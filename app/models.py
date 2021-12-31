from app import db
import datetime

# 修改响应状态为成功
def change_msg(res):
    res['msg'] = "success"
    res['flag'] = 1
    return res

# def change_topic_flag(res):
#     res[0]['msg'] = "success"
#     res[0]['flag'] = 1
#     return res

class Topic(db.Model):
    """课题"""
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    topicname = db.Column(db.String(128), unique=True, nullable=False)  # 课题名词
    uuid = db.Column(db.String(128), unique=True)  # 课题唯一UUID
    status = db.Column(db.Boolean, default=False)  # 课题通过状态
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))  # 课题所属学生

    def to_json(self):
        result = {
            'topicinfo': [
                {
                    'topicname': self.topicname,
                    'uuid': self.uuid,
                    'status': self.status,
                    'student': self.stutopic.username,
                    'student_id': self.student_id
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
        return self.uuid


class Paper(db.Model):
    """论文"""
    __tablename__ = 'paper'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(128), nullable=False)  # 文件名
    uuid = db.Column(db.String(128), unique=True)  # 文件名生成的uuid
    status = db.Column(db.Boolean, default=False)  # 论文状态
    path = db.Column(db.String(265))  # 文件路径
    date = db.Column(db.DateTime, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # 保存上传时间
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))  # 论文对应的学生

    def to_json(self):
        result = {
            'paperinfo': [
                {
                    'id': self.id,
                    'filename': self.filename,
                    'uuid': self.uuid,
                    'status': self.status,
                    'student': self.stupaper.username if self.stupaper is not None else None,
                    'student_id': self.student_id,
                    'path': self.path,
                    'date': self.date
                },
            ],
            "msg": "",
            "flag": 0
        }
        return result

    def save_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return self.uuid


class User(db.Model):
    """管理员"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)  # 用户名
    password = db.Column(db.String(64))  # 密码
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 所属角色

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
    username = db.Column(db.String(64))  # 教师名
    password = db.Column(db.String(64))  # 密码
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 属实角色
    students = db.relationship(
        'Student',
        backref='teac',
        lazy='dynamic')  # 指导的学生

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
                    'students': studentlist,
                    'role_id': self.role_id,
                    'role': self.teacher.name if self.teacher is not None else None
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
    username = db.Column(db.String(64))  # 学生名
    password = db.Column(db.String(64))  # 密码
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 角色
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))  # 所属教师
    # topics = db.relationship('Topic', backref='stu', lazy='dynamic')  # 课题
    topics = db.relationship(
        'Topic',
        foreign_keys=[Topic.student_id],
        backref=db.backref('stutopic', lazy='joined'),
        lazy='dynamic',
        cascade='all, delete-orphan'
    ) # 申请的课题
    papers = db.relationship(
        'Paper',
        foreign_keys=[Paper.student_id],
        backref=db.backref('stupaper', lazy='joined'),
        lazy='dynamic',
        cascade='all, delete-orphan'
    ) # 上传的论文

    # 序列化
    def to_json(self):
        # 获取学生课题列表
        topiclist = []
        for i in self.topics.all():
            topiclist.append(str(i))


        paperlist = []
        for i in self.papers.all():
            paperlist.append(str(i))
        # 响应信息
        result = {
            'studentinfo': [
                {
                    'id': self.id,
                    'username': self.username,
                    'password': self.password,
                    'teacher': self.teac.username if self.teac is not None else None,
                    'topics': topiclist,
                    'papers': paperlist,
                    'role_id': self.role_id,
                    'role': self.student.name if self.student is not None else None,
                    'teacher_id': self.teacher_id
                }],
            'msg': "",
            'flag': 0}
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


class Role(db.Model):
    """角色"""
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)  # 角色名
    default = db.Column(db.Boolean, default=False, index=True)  # 默认角色
    permissions = db.Column(db.Integer)  # 权限
    # users = db.relationship('User', backref='role', lazy='dynamic')
    # 所属管理员的用户
    users = db.relationship(
        'User',
        foreign_keys=[User.role_id],
        backref=db.backref('admin', lazy='joined'),
        lazy='dynamic',
        cascade='all, delete-orphan'
    )
    # 所属教师的用户
    teachers = db.relationship(
        'Teacher',
        foreign_keys=[Teacher.role_id],
        backref=db.backref('teacher', lazy='joined'),
        lazy='dynamic',
        cascade='all, delete-orphan'
    )
    # 所属学生的用户
    students = db.relationship(
        'Student',
        foreign_keys=[Student.role_id],
        backref=db.backref('student', lazy='joined'),
        lazy='dynamic',
        cascade='all, delete-orphan'
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
