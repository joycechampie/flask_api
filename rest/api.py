from flask import Flask
from flask_restx import Api
from rest.endpoints.student.namespace import api as student_api
from rest.endpoints.city.namespace import api as city_api

app = Flask(__name__)
api = Api(app)

api.add_namespace(student_api)
api.add_namespace(city_api)

