#!/usr/bin/python3
""" views functionality """
from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# Define a route /status on the app_views Blueprint
@app_views.route('/status', methods=['GET'])
def status():
    """Return status OK on route /status"""
    return jsonify({"status": "OK"})

# Define a route /stats on the app_views Blueprint
@app_views.route('/stats', methods=['GET'])
def stats():
    """Return count of all objects per class"""
    # Define classes and corresponding models
    classes = {"amenities": Amenity, "cities": City, "places": Place,
               "reviews": Review, "states": State, "users": User}

    # Count objects for each class using storage.count()
    obj_count = {key: storage.count(value) for key, value in classes.items()}

    # Return the object count as a JSON response
    return make_response(jsonify(obj_count))
