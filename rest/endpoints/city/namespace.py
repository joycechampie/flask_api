from flask_restx import Namespace

from rest.endpoints.city.city import City

# Namespace allows you to create urls for your Resource(City)
api = Namespace(name= "City", path="/api/city")

# add_resource lets you add your resource to the Namespace
# methods allows you to specify the CRUD operations the endpoint can perform
api.add_resource(City, "/records/<name>", methods=["GET"])
api.add_resource(City, "/records", methods=["POST"])