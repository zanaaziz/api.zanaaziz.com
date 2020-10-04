from flask_restful import Resource, request
from flask_jwt_extended import jwt_required
from models.item import ItemModel
from schemas.item import ItemSchema

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)

class ItemsList(Resource):
	@classmethod
	def get(cls):
		items = item_list_schema.dump(ItemModel.find_all())

		if len(items) > 0:
			return { 'items': items }, 200

		return { 'message': 'No items available.' }, 200

	@classmethod
	def post(cls):
		item_req_model = item_schema.load(request.get_json())
		
		try:
			item_req_model.save()
		except:
			return { 'message': 'Error while creating item.' }, 500

		return { 'message': 'Item created.', 'item': item_schema.dump(item_req_model) }, 201


class Items(Resource):
	@classmethod
	def get(cls, _id: int):
		try:
			item = ItemModel.find_by_id(_id=_id)
		except:
			return { 'message': 'Error while finding item.' }, 500

		if item:
			return item_schema.dump(item), 200

		return { 'message': 'Item not found.' }, 404

	@classmethod
	def put(cls, _id: int):
		try:
			item_to_update = ItemModel.find_by_id(_id=_id)
		except:
			return { 'message': 'Error while finding item.' }, 500

		if item_to_update is None:
			return { 'message': 'Item not found.' }, 404

		item_req_model = item_schema.load(request.get_json(), instance=item_to_update)
		
		try:
			item_req_model.save()
		except:
			return { 'message': 'Error while updating item.' }, 500

		return { 'message': 'Item updated.', 'item': item_schema.dump(item_req_model) }, 200

	@classmethod
	@jwt_required
	def delete(cls, _id: int):
		try:
			item = ItemModel.find_by_id(_id=_id)
		except:
			return { 'message': 'Error while finding item.' }, 500

		if item is None:
			return { 'message': 'Item not found.' }, 404

		try:
			item.delete()
		except:
			return { 'message': 'Error while deleting item.' }, 500

		return { 'message': 'Item deleted.' }, 200
