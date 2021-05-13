from .data import persons
from flask_restful import Resource


class Persons(Resource):

    def get(self):
        return persons
