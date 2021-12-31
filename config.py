"""配置文件"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """配置参数类"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asolmn'

    DB = 'mysql+pymysql'
    NAME = 'root'
    PWD = '123456'
    HOST = 'localhost'
    DBNAME = 'paperos'
    UPLOAD_FOLDER = 'D:/Project/PaperOS/uploads'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """开发环境"""
    DEBUG = True
    # 测试环境中使用内存中的数据库，测试运行后无需保留任何数据，所以不用数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              "{}://{}:{}@{}/{}".format(Config.DB, Config.NAME, Config.PWD, Config.HOST, Config.DBNAME)



class TestingConfig(Config):
    """测试环境"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'

class ProductionConfig(Config):
    """生产环境"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


# 设置默认环境
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
