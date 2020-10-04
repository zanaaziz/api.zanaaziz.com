from db import db
from typing import List

class StoreModel(db.Model):
	__tablename__ = 'stores'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)

	items = db.relationship('ItemModel', lazy='dynamic')

	def save(self) -> None:
		db.session.add(self)
		db.session.commit()

	def delete(self) -> None:
		db.session.delete(self)
		db.session.commit()

	@classmethod
	def find_all(cls) -> List['StoreModel']:
		return cls.query.all()

	@classmethod
	def find_by_id(cls, _id: int) -> 'StoreModel':
		return cls.query.filter_by(id=_id).first()
