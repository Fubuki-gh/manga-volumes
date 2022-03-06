from datetime import date, datetime
import sqlite3
from flask_restful import Resource, fields, marshal_with, reqparse

get_parser = reqparse.RequestParser()
get_parser.add_argument(
    'name', dest='name',
    location='args', required=True,
    help='Name of title'
)

title_fields = {
    'name': fields.String
}

class TitleSearch(Resource):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.db: sqlite3.Connection = kwargs['db']
    #@marshal_with(title_fields)
    def get(self):
        args = get_parser.parse_args()
        cursor = self.db.cursor()
        cursor.execute(f"""SELECT * FROM 'Title'
        WHERE name LIKE '{args['name']}'""")

        result = cursor.fetchall()
        print(result)

        cursor.close()
        return result, 200