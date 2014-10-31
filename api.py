from flask import Flask
from flask.ext import restful
from flask_cors import CORS

from config import settings

FASTLANE = Flask(__name__)
CORS_FASTLANE = CORS(FASTLANE)


if settings.DEBUG:
    FASTLANE.debug = True

FASTLANE_API = restful.Api(FASTLANE)

from endpoints import ALL_ENDPOINTS

for endpoint in ALL_ENDPOINTS:
    FASTLANE_API.add_resource(endpoint, '/api/' + settings.BASE_API_VERSION + endpoint.location)

if __name__ == '__main__':
    FASTLANE.run(port=5002)