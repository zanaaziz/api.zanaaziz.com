from db import db

class UserModel(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(80), nullable=False, unique=True)
	password = db.Column(db.String(80), nullable=False)

	def save(self) -> None:
		db.session.add(self)
		db.session.commit()

	def delete(self) -> None:
		db.session.delete(self)
		db.session.commit()

	@classmethod
	def find_by_id(cls, _id: int) -> 'UserModel':
		return cls.query.filter_by(id=_id).first()

	@classmethod
	def find_by_email(cls, email: str) -> 'UserModel':
		return cls.query.filter_by(email=email).first()
