from flask import request, abort
from flask_restful import Resource
from marshmallow import Schema, fields

class Title(Resource):
    def get(self, title_id):
        return {"data": f"{title_id}"}, 200

class TitleQuerySchema(Schema):
    name = fields.Str(required=True)
    limit = fields.Int(required=False)
    offset = fields.Int(required=False)
    sort = fields.Str(required=False)

class TitleQ(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.schema = TitleQuerySchema()
    def get(self):
        errors = self.schema.validate(request.args)
        if errors:
            abort(400, str(errors))
        name = request.args.get("name", type=str)
        limit = request.args.get("limit", type=int, default=20)
        offset = request.args.get("offset", type=int, default=0)
        sort = request.args.get("sort", type=str, default=None)

        return {"data": {
            "name": name,
            "limit": limit,
            "offset": offset,
            "sort": sort}}, 200