__author__ = 'gsibble'

from flask.ext.restful import reqparse, Resource

from models import sql_models

class ApiEndpoint(Resource):
    models = sql_models

    def options(self, *args, **kwargs):
        #result = API_Result(success=True, status_code=200, result='')
        return self.make_html_response('')

    def make_response(self, api_result, response_code, *args, **kwargs):
        headers = {}
        headers['Allow'] = 'GET, POST, PUT, DELETE, OPTIONS'
        headers['Access-Control-Allow-Origin'] = '*'
        headers['Access-Control-Max-Age'] = str(1728000)
        headers['Access-Control-Allow-Headers'] = 'accept, origin, api_key, content-type, Api-Key'
        headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        return api_result, response_code, headers


    def make_html_response(self, html, *args, **kwargs):
        headers = {}
        headers['Allow'] = 'GET, POST, PUT, DELETE, OPTIONS'
        headers['Access-Control-Allow-Origin'] = '*'
        headers['Access-Control-Max-Age'] = str(1728000)
        headers['Access-Control-Allow-Headers'] = 'accept, origin, api_key, content-type, Api-Key'
        headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        return (html, 200, headers)