#!/usr/bin/python3
"""Flask API to return status"""

from flask import Flask, jsonify, make_response
from flask_cors import CORS
from models import storage
from os import getenv
from api.v1.views import app_views

# Create a Flask application instance
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing)
CORS(app, origins='0.0.0.0')

# Register the blueprint for API endpoints
app.register_blueprint(app_views)

# Define a method to handle teardown of the Flask application context
@app.teardown_appcontext
def teardown(exception):
    """Destroys DB session in case of DB storage,
    reloads objects in case of File Storage"""
    storage.close()

# Define an error handler for 404 Not Found errors
@app.errorhandler(404)
def error_404(error):
    """Response for 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)


# Run the Flask application
if __name__ == "__main__":
    # Get host address from environ variable HBNB_API_HOST/default to '0.0.0.0'
    host = getenv('HBNB_API_HOST') or '0.0.0.0'

    # Get port number from environment variable HBNB_API_PORT/default to 5000
    port = int(getenv('HBNB_API_PORT') or 5000)

    # Start the Flask server
    app.run(host=host, port=port, threaded=True)
