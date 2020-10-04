from db import db
from typing import List

class ItemModel(db.Model):
	__tablename__ = 'items'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	color = db.Column(db.String(80), nullable=False)

	store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
	store = db.relationship('StoreModel')

	def save(self) -> None:
		db.session.add(self)
		db.session.commit()

	def delete(self) -> None:
		db.session.delete(self)
		db.session.commit()

	@classmethod
	def find_all(cls) -> List['ItemModel']:
		return cls.query.all()

	@classmethod
	def find_by_id(cls, _id: int) -> 'ItemModel':
		return cls.query.filter_by(id=_id).first()
