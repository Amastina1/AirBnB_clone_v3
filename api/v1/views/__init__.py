""" init file for views module """
from flask import Blueprint
# Import all views from index.py (PEP8 will complain, but it's normal)
from api.v1.views.index import *
from api.v1.views import (amenities, cities, places, places_amenities,
                          places_reviews, states, users)*

# Create a Blueprint instance for views with URL prefix /api/v1
app_views = Blueprint('views', __name__, url_prefix="/api/v1")
