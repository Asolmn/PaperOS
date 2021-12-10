from flask import Blueprint


auth = Blueprint('auth', __name__)

print("success")

from . import views