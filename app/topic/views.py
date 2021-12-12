from flask import request, jsonify
from app.auth import auth
from app.models import Role, User, Student, Teacher, change_msg
