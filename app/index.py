from flask import Blueprint
from flask_restful import Api, Resource

index = Blueprint('index', __name__)
api = Api(index)


class IndexApi(Resource):
    def get(self):
        return "Hello World!"


api.add_resource(IndexApi, '/')
