from flask_restful import Resource
from .data import tasks


class Tasks(Resource):

    def get(self):
        return tasks
