from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, fields, marshal_with, reqparse

from api.models.models import TitleModel


get_parser_title_search = reqparse.RequestParser()
get_parser_title_search.add_argument(
    'name', dest='name',
    location='args', required=True,
    help='Missing \'name\' parameter'
)
get_parser_title_search.add_argument(
    'limit', dest='limit',
    location='args', required=False,
    type=int, default=10
)

title_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'synopsis': fields.String,
    'start_date': fields.Integer,
    'end_date': fields.Integer,
    'chapter_count': fields.Integer,
    'volume_count': fields.Integer
}

class TitleSearch(Resource):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.db: SQLAlchemy = kwargs['db']

    @marshal_with(title_fields)
    def get(self):
        args = get_parser_title_search.parse_args()

        search  = '%{}%'.format(args.name)
        limit   = args['limit']
        result  = TitleModel.query.filter(TitleModel.name.like(search)).limit(limit).all()

        if len(result) == 0:
            return result, 404

        return result, 200

class Title(Resource):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.db: SQLAlchemy = kwargs['db']

    @marshal_with(title_fields)
    def get(self, id):
        
        result = TitleModel.query.filter_by(id=id).first()

        if result is None:
            return result, 404

        return result, 200