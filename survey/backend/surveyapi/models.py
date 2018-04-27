"""
survey/backend/surveyapi/models.py
定义数据模型
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Survey(db.Model):
    __tablename__ = 'surveys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    questions = db.relationship('Question', backref="survey", lazy=False)
    # 与Question表做外键关联

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            questions=[question.to_dict() for question in self.questions]
        )

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    survey_id = db.Column(db.Integer, db.ForeignKey('surveys.id'))
    # 获取surveys表的id值
    choices = db.relationship('Choice', backref="question", lazy=False)
    # 与Choice表做外键关联
    
    def to_dict(self):
        return dict(
            id=self.id,
            text=self.text,
            created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            survey_id=self.survey_id,
            choices=[choice.to_dict() for choice in self.choices]
        )

class Choice(db.Model):
    __tablename__ = 'choices'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    selected = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    # 获取questions表的id值    
    
    def to_dict(self):
        return dict(
            id=self.id,
            text=self.text,
            selected = self.selected,
            created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            question_id=self.question_id
        )
