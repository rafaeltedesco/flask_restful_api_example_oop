from .data import persons
from flask import jsonify
from flask_restful import Resource, reqparse, abort

parser = reqparse.RequestParser()
parser.add_argument('name')


class Person:

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Persons(Resource):

    def get(self):
        return persons

    def post(self):
        args = parser.parse_args()
        person_id = len(persons) + 1
        new_person = Person(person_id, args['name'])
        persons.append({
            'id': new_person.id,
            'name': new_person.name
        })
        return {
            "status": "OK",
            "message": "New Person created"
        }
