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
def stats():
    '''retrieves the number of each objects by type'''
    result = {}
    for clss in classes:
        counter = storage.count(classes[clss])
        result[clss] = counter
    return jsonify(result)
