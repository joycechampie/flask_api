from flask_restx import Resource


class Student(Resource):
     def get(self, name):
         return name

     def post(self):
         return "created"