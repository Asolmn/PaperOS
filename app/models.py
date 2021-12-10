from app import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    # 返回序列化
    def to_json(self):
        users = []
        # 获取当前角色下的所有用户
        for i in self.users.all():
            users.append(str(i))
        result = {
            'roleinfo': [
                {
                    'id': self.id,
                    'name': self.name,
                    'permissions': self.permissions,
                    'users': users
                }
            ],
            'msg': "",
            'flag': 0
        }
        return result

    def msg_flag(res):
        res['msg'] = "success"
        res['flag'] = '1'

        return res

    def __repr__(self):
        return self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # 返回序列化
    def to_json(self):
        result = {
            'userinfo': [
                {
                    'id': self.id,
                    'username': self.username,
                    'password': self.password,
                    'role': self.role_id
                }
            ],
            'msg': "",
            'flag': 0
        }
        return result


    def save_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return self.username

