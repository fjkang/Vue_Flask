"""
survey/backend/surveyapi/api.py
提供API路由,定义REST的请求和响应
"""

from flask import Blueprint, jsonify, request
from surveyapi.models import db, Survey, Question, Choice

api = Blueprint('api', __name__)


@api.route('/hello/<string:name>/')
def say_hello(name):
    response = {'msg': f"Hello {name}."}
    return jsonify(response)


@api.route('/surveys/', methods=['GET', 'POST'])
def surveys():
    if request.method == 'GET':
        surveys = Survey.query.all()
        return jsonify({'surveys': [s.to_dict() for s in surveys]})
    elif request.method == 'POST':
        data = request.get_json()
        survey = Survey(name=data['name'])
        questions = []
        for q in data['questions']:
            question = Question(text=q['question'])
            question.choices = [Choice(text=c) for c in q['choices']]
            questions.append(question)

        survey.questions = questions
        db.session.add(survey)
        db.session.commit()
        return jsonify(survey.to_dict()), 201


@api.route('/surveys/<int:id>/', methods=['GET', 'PUT'])
def survey(id):
    if request.method == 'GET':
        survey = Survey.query.get(id)
        return jsonify({'survey': survey.to_dict()})
    elif request.method == 'PUT':
        data = request.get_json()
        for q in data['questions']:
            choice = Choice.query.get(q['choice'])
            choice.selected = choice.selected + 1
        db.session.commit()
        survey = Survey.query.get(data['id'])
        return jsonify(survey.to_dict()), 201
