from flask_jwt_extended import create_access_token
from flask import Response, request
from flask_restful import Resource, reqparse
from flask_cors import cross_origin

parser = reqparse.RequestParser()

class SignUpApi(Resource):
    @cross_origin
    def post(self):
        try:
            body = request.get_json()
        except Exception:
            return "Error"