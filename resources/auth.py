from flask import Response, request,jsonify
from flask_jwt_extended import create_access_token,create_refresh_token
from database.models import User
from flask_restful import Resource
import datetime

class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user =  User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200

class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if authorized:
            access_token = create_access_token(identity=user.email, fresh=True)
            refresh_token = create_refresh_token(identity=user.email)                        
            return jsonify(access_token=access_token, refresh_token=refresh_token)
        else:
            return jsonify({"status":authorized})