from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError

from db import db
from ma import ma
from blacklist import BLACKLIST

from resources.user import UserLogin, UserLogout, UserTokenRefresh
from resources.post import Posts, PostsList

sqlite_db = 'sqlite:///data.db'
staging_db = 'mysql+mysqlconnector://root:root@127.0.0.1:8889/blog'
production_db = 'mysql+mysqlconnector://zanaynnp_zana:NJmZnT2g4uHDf7C@127.0.0.1:3306/zanaynnp_blog'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = production_db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_SECRET_KEY'] = 'secret'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
api = Api(app)
jwt = JWTManager(app)

@app.errorhandler(ValidationError)
def marshmallow_validation_error(err):
	return jsonify(err.messages), 400

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
	if identity == 1:
		return { 'is_root': True }
	else:
		return { 'is_root': False }

@jwt.token_in_blacklist_loader
def token_in_blacklist(decrypted_token):
	return decrypted_token['jti'] in BLACKLIST

@jwt.expired_token_loader
def expired_token():
	return { 'error': 'expired_token', 'message': 'Token has expired.' }, 401

@jwt.needs_fresh_token_loader
def needs_fresh_token():
	return { 'error': 'fresh_token_required', 'message': 'Fresh token needed, re-login to acquire.' }, 401

@jwt.revoked_token_loader
def revoked_token():
	return { 'error': 'revoked_token', 'message': 'Token no longer valid.' }, 401

@jwt.invalid_token_loader
def invalid_token(error):
	return { 'error': 'invalid_token', 'message': 'Signature verification failed.' }, 401

@jwt.unauthorized_loader
def unauthorized(error):
	return { 'error': 'authorization_required', 'message': 'No valid authorization method detected.' }, 401

@app.before_first_request
def create_database_tables():
	db.create_all()

api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(UserTokenRefresh, '/refresh')
api.add_resource(PostsList, '/posts')
api.add_resource(Posts, '/posts/<int:_id>')

if __name__ == '__main__':
	db.init_app(app)
	ma.init_app(app)
	app.run(port=5000, debug=True)
