"""
survey/backend/surveyapi/config.py
flask的配置文件
"""
import os
# 数据库的设置
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'survey.db')

class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'ni cai bu dao de!'

