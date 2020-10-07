from db import db

class UserModel(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), nullable=False, unique=True)
	password = db.Column(db.String(80), nullable=False)

	@classmethod
	def find_by_username(cls, username: str) -> 'UserModel':
		return cls.query.filter_by(username=username).first()
