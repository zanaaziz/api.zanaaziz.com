from flask_restful import Resource, request
from datetime import timedelta
from models.user import UserModel
from schemas.user import UserSchema
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST
from flask_jwt_extended import (
	create_access_token,
	create_refresh_token,
	jwt_required,
	get_jwt_claims,
	jwt_refresh_token_required,
	get_jwt_identity,
	fresh_jwt_required,
	get_raw_jwt,
	get_jti
)

user_schema = UserSchema()


class UserLogin(Resource):
	@classmethod
	def post(cls):
		user_req_model = user_schema.load(request.get_json())
		
		try:
			user = UserModel.find_by_username(username=user_req_model.username)
		except:
			return { 'message': 'Error while finding user.' }, 500

		if user is None:
			return { 'message': 'Invalid username.' }, 401

		if safe_str_cmp(user.password, user_req_model.password):
			return {
				'id': user.id,
				'access_token': create_access_token(identity=user.id, fresh=True, expires_delta=timedelta(minutes=30)),
				'refresh_token': create_refresh_token(identity=user.id, expires_delta=False)
			}, 200

		return { 'message': 'Invalid password.' }, 401


class UserLogout(Resource):
	@classmethod
	@jwt_required
	def post(cls):
		access_jti = get_raw_jwt()['jti']

		body = request.get_json()
		refresh_jti = get_jti(encoded_token=body['refresh_token'])

		BLACKLIST.add(access_jti)
		BLACKLIST.add(refresh_jti)

		return { 'message': 'User logged out.' }, 200


class UserTokenRefresh(Resource):
	@classmethod
	@jwt_refresh_token_required
	def post(cls):
		return { 'access_token': create_access_token(identity=get_jwt_identity(), fresh=False, expires_delta=timedelta(minutes=30)) }, 200

