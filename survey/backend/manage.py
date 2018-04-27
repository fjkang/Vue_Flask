"""
survey/backend/manage.py
创建数据库等命令行管理工具
"""

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from surveyapi.application import create_app
from surveyapi.models import db, Survey, Question, Choice

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.shell
def shell_ctx():
    return dict(
        app=app,
        db=db,
        Survey=Survey,
        Question=Question,
        Choice=Choice
    )

if __name__ == '__main__':
    manager.run()