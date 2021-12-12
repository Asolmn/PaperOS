from flask import Blueprint


paper = Blueprint('paper', __name__)

print("success")


from . import views