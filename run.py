import os
from app import create_app, db
from app.models import Role, User, Student, Teacher, Topic
from flask_migrate import Migrate


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Role=Role, User=User, Student=Student, Teacher=Teacher, Topic=Topic)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    app.debug(True)
