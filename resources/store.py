from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, jwt_optional, get_jwt_identity
from models.store import StoreModel
from schemas.store import StoreSchema

store_schema = StoreSchema()
store_list_schema = StoreSchema(many=True)

class StoresList(Resource):
	@classmethod
	@jwt_optional
	def get(cls):
		user_id = get_jwt_identity()

		stores = store_list_schema.dump(StoreModel.find_all())

		if len(stores) == 0:
			return { 'message': 'No stores available.' }, 200

		if user_id:
			return { 'stores': stores }, 200

		return { 'stores': [store['name'] for store in stores] }, 200

	@classmethod
	def post(cls):
		store_req_model = store_schema.load(request.get_json())
		
		try:
			store_req_model.save()
		except:
			return { 'message': 'Error while creating store.' }, 500

		return { 'message': 'Store created.', 'store': store_schema.dump(store_req_model) }, 201


class Stores(Resource):
	@classmethod
	def get(cls, _id: int):
		try:
			store = StoreModel.find_by_id(_id=_id)
		except:
			return { 'message': 'Error while finding store.' }, 500

		if store:
			return store_schema.dump(store), 200

		return { 'message': 'Store not found.' }, 404

	@classmethod
	def put(cls, _id: int):
		try:
			store_to_update = StoreModel.find_by_id(_id=_id)
		except:
			return { 'message': 'Error while finding store.' }, 500

		if store_to_update is None:
			return { 'message': 'Store not found.' }, 404

		store_req_model = store_schema.load(request.get_json(), instance=store_to_update)
		
		try:
			store_req_model.save()
		except:
			return { 'message': 'Error while updating store.' }, 500

		return { 'message': 'Store updated.', 'store': store_schema.dump(store_req_model) }, 200

	@classmethod
	@jwt_required
	def delete(cls, _id: int):
		try:
			store = StoreModel.find_by_id(_id=_id)
		except:
			return { 'message': 'Error while finding store.' }, 500

		if store is None:
			return { 'message': 'Store not found.' }, 404

		try:
			store.delete()
		except:
			return { 'message': 'Error while deleting store.' }, 500

		return { 'message': 'Store deleted.' }, 200
