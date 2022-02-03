import sys 
from typing import List
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

#Resource
class Test(Resource):
    def get(self, name) -> dict:
        return {"name": name}

#Register resource
api.add_resource(Test, "/test/<string:name>")

#Main
def main(argc: int, argv: list[str]) -> None:
    if argc < 2:
        app.run(debug=False)
    elif argv[1] == "debug":
        app.run(debug=True)
    else:
        app.run(debug=False)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
