from flask_restful import Resource
from .treemap import urls


class Home(Resource):

    def get(self):
        return urls
