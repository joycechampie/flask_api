from flask_restx import Resource


class City(Resource):
    def get(self, name):
        return name

    def post(self):
        return "created"