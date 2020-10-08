from db import db
from typing import List
from sqlalchemy.sql import func
from sqlalchemy import desc
import datetime

class PostModel(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(300), nullable=False)
	image_url = db.Column(db.String(600), default='')
	body = db.Column(db.Text(4294000000), nullable=False)
	date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
	live = db.Column(db.Boolean, default=False)

	def save(self) -> None:
		db.session.add(self)
		db.session.commit()

	def delete(self) -> None:
		db.session.delete(self)
		db.session.commit()

	def json(self):
		return {
			'id': self.id,
			'title': self.title,
			'image_url': self.image_url,
			'body': self.body,
			'date_created': self.date_created.strftime("%Y-%m-%dT%H:%M:%S"),
			'live': self.live
		}

	@classmethod
	def find_all(cls) -> List['PostModel']:
		return cls.query.order_by(desc(cls.date_created)).all()

	@classmethod
	def find_all_live(cls) -> List['PostModel']:
		return cls.query.filter_by(live=True).order_by(desc(cls.date_created)).all()

	@classmethod
	def find_by_id(cls, _id: int) -> 'PostModel':
		return cls.query.filter_by(id=_id).first()
