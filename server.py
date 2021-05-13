from flask import Flask
from flask_restful import Api, Resource


class TaskApi:

    def __init__(self):
        self._app = Flask(__name__)
        self._api = Api(self._app)

    def start(self, debug: bool = False):
        self._app.run(debug=debug)

    def add_resource(self, resource: Resource, path: str):
        self._api.add_resource(resource, path)
