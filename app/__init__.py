from flask import Flask, render_template
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth/')

    return app