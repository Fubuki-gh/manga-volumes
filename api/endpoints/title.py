from msilib import schema
from flask import request, abort
from flask_restful import Resource
from marshmallow import Schema, fields

class Title(Resource):
    def get(self, title_id):
        return {"data": f"{title_id}"}, 200

class TitleQuerySchema(Schema):
    name = fields.Str(required=True)

class TitleQ(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.schema = TitleQuerySchema()
    def get(self):
        errors = self.schema.validate(request.args)
        if errors:
            abort(400, str(errors))
        title_name = request.args.get("name", type=str)
        return {"data": f"{title_name}"}, 200