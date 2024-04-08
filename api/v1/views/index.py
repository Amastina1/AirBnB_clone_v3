#!/usr/bin/python3
'''index blueprint'''

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    '''returns json object with the app status'''
    return jsonify({"status": "OK"})

@app_views.route('/stats')
def get_stats():
    '''returns the number of each object by type'''
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)
