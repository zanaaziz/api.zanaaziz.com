from ma import ma
from models.post import PostModel

class PostSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = PostModel
		load_instance = True
