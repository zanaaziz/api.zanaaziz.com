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

class UserRegister(Resource):
	@classmethod
	def post(cls):
		user_req_model = user_schema.load(request.get_json())

		try:
			if UserModel.find_by_email(email=user_req_model.email):
				return { 'message': 'Email already in use.' }, 409
		except:
			return { 'message': 'Error while isolating user.' }, 500
		
		try:
			user_req_model.save()
		except:
			return { 'message': 'Error while creating user.' }, 500

		return {
			'message': 'User created.',
			'user': user_schema.dump(user_req_model),
			'access_token': create_access_token(identity=user_req_model.id, fresh=True, expires_delta=timedelta(minutes=30)),
			'refresh_token': create_refresh_token(identity=user_req_model.id, expires_delta=False)
		}, 201


class UserLogin(Resource):
	@classmethod
	def post(cls):
		user_req_model = user_schema.load(request.get_json())
		
		try:
			user = UserModel.find_by_email(email=user_req_model.email)
		except:
			return { 'message': 'Error while finding user.' }, 500

		if user is None:
			return { 'message': 'Invalid email.' }, 401

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


class User(Resource):
	@classmethod
	def get(cls, _id: int):
		try:
			user = UserModel.find_by_id(_id=_id)
		except:
			return { 'message': 'Error while finding user.' }, 500

		if user is None:
			return { 'message': 'User not found.' }, 404

		return user_schema.dump(user), 200

	@classmethod
	@jwt_required
	@fresh_jwt_required
	def delete(cls, _id: int):
		claims = get_jwt_claims()
		if not claims['is_root']:
			return { 'message': 'Access denied due to missing priveleges.' }, 401

		try:
			user = UserModel.find_by_id(_id=_id)
		except:
			return { 'message': 'Error while finding user.' }, 500

		if user is None:
			return { 'message': 'User not found.' }, 404

		try:
			user.delete()
		except:
			return { 'message': 'Error while deleting user.' }, 500

		return { 'message': 'User deleted.' }, 200
