from flask import Flask, render_template, abort
from flask_pymongo import PyMongo
from flask_restful import Api, Resource, reqparse, fields
from flask_cors import CORS

app = Flask(__name__)

app.config.update(MONGO_URI='mongodb://localhost:27017/Computers')

mongo = PyMongo(app)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

computers_fields = {
    
}

class ComputerList(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', location='json')
        self.parser.add_argument('department', location='json')
        self.parser.add_argument('user', location='json')
        self.parser.add_argument('type', location='json')
        self.parser.add_argument('cpu', location='json')
        self.parser.add_argument('memory', location='json')
        self.parser.add_argument('buydate', location='json')
        self.parser.add_argument('price', location='json')
        self.parser.add_argument('used', location='json')
        super(ComputerList, self).__init__()

    def get(self):
        query = {}
        projection = {"_id": 0}
        computers = [
            data for data in mongo.db.computers.find(query, projection)
        ]
        return {'computers': computers}

    def post(self):
        args = self.parser.parse_args()
        id = args['id']
        computer = dict(
            id=args['id'],
            department=args['department'],
            user=args['user'],
            type=args['type'],
            cpu=args['cpu'],
            memory=args['memory'],
            buydate=args['buydate'],
            price=args['price'],
            used=args['used'])
        mongo.db.computers.insert(computer)
        return {'msg': f"添加{id}成功!"}


class Computer(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        # self.parser.add_argument('computer') # 使用...展开后,不需要后台处理json了
        self.parser.add_argument('id', location='json')
        self.parser.add_argument('department', location='json')
        self.parser.add_argument('user', location='json')
        self.parser.add_argument('type', location='json')
        self.parser.add_argument('cpu', location='json')
        self.parser.add_argument('memory', location='json')
        self.parser.add_argument('buydate', location='json')
        self.parser.add_argument('price', location='json')
        self.parser.add_argument('used', location='json')
        super(Computer, self).__init__()

    def get(self, id):
        query = {"id": id}
        projection = {"_id": 0}
        computer = mongo.db.computers.find_one_or_404(query, projection)
        return {'computer': computer}

    def put(self, id):
        query = {"id": id}
        projection = {"_id": 0}
        computer = mongo.db.computers.find_one_or_404(query, projection)
        args = self.parser.parse_args()
        # computer_data = json.loads(args['computer'].replace('\'', '\"')) # 需要把'替换成"才能完成str->json->dict的转换
        for key, value in args.items():
            if value != None:
                computer[key] = value
        mongo.db.computers.update(query, {"$set": computer})
        return {'msg': f"修改{id}成功!"}

    def delete(self, id):
        query = {"id": id}
        projection = {"_id": 0}
        computer = mongo.db.computers.find_one_or_404(query, projection)
        mongo.db.computers.remove({"id": id})
        return {'msg': f"删除{id}成功!"}


api.add_resource(ComputerList, '/api/computers', endpoint='computers')
api.add_resource(Computer, '/api/computers/<id>', endpoint='computer')

if __name__ == '__main__':
    app.run(debug=True)
