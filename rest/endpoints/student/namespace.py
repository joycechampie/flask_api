from flask_restx import Namespace

from rest.endpoints.student.student import Student


api = Namespace("Student" , path="/api/student")
api.add_resource(Student, "/records/<name>", methods=["GET"])
api.add_resource(Student,"/records", methods=["POST"])


