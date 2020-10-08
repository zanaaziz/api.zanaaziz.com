from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, jwt_optional, get_jwt_identity
from models.post import PostModel
from schemas.post import PostSchema

post_schema = PostSchema()
post_list_schema = PostSchema(many=True)

class PostsList(Resource):
	@classmethod
	@jwt_optional
	def get(cls):
		user_id = get_jwt_identity()

		if user_id:
			posts = post_list_schema.dump(PostModel.find_all())
		else:
			posts = post_list_schema.dump(PostModel.find_all_live())

		if len(posts) > 0:
			return { 'posts': posts }, 200

		return { 'message': 'No posts available.' }, 200

	@classmethod
	@jwt_required
	def post(cls):
		post_req_model = post_schema.load(request.get_json())
		
		try:
			post_req_model.save()
		except:
			return { 'message': 'Error while creating post.' }, 500

		return { 'message': 'Post created.', 'post': post_schema.dump(post_req_model) }, 201


class Posts(Resource):
	@classmethod
	def get(cls, _id: int):
		try:
			post = PostModel.find_by_id(_id=_id)
		except:
			return { 'message': 'Error while finding post.' }, 500

		if post:
			return post_schema.dump(post), 200

		return { 'message': 'Post not found.' }, 404

	@classmethod
	@jwt_required
	def put(cls, _id: int):
		try:
			post_to_update = PostModel.find_by_id(_id=_id)
		except:
			return { 'message': 'Error while finding post.' }, 500

		if post_to_update is None:
			return { 'message': 'Post not found.' }, 404

		post_req_model = post_schema.load(request.get_json(), instance=post_to_update)
		
		try:
			post_req_model.save()
		except:
			return { 'message': 'Error while updating post.' }, 500

		return { 'message': 'Post updated.', 'post': post_schema.dump(post_req_model) }, 200

	@classmethod
	@jwt_required
	def delete(cls, _id: int):
		try:
			post = PostModel.find_by_id(_id=_id)
		except:
			return { 'message': 'Error while finding post.' }, 500

		if post is None:
			return { 'message': 'Post not found.' }, 404

		try:
			post.delete()
		except:
			return { 'message': 'Error while deleting post.' }, 500

		return { 'message': 'Post deleted.' }, 200


class PostsToggleLive(Resource):
	@classmethod
	@jwt_required
	def put(cls, _id: int):
		try:
			post_to_update = PostModel.find_by_id(_id=_id)
		except:
			return { 'message': 'Error while finding post.' }, 500

		if post_to_update is None:
			return { 'message': 'Post not found.' }, 404

		updated_post = post_to_update
		updated_post.live = not updated_post.live

		print(updated_post.json())

		post_req_model = post_schema.load(updated_post.json(), instance=post_to_update)
		
		try:
			post_req_model.save()
		except:
			return { 'message': 'Error while updating post.' }, 500

		return { 'message': 'Post updated.', 'post': post_schema.dump(post_req_model) }, 200
