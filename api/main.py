import sys
from flask import Flask
from flask_restful import Api

from endpoints.title import TitleQ, Title

#Main
def main(argc: int, argv: list[str]) -> None:

    app = Flask(__name__)
    api = Api(app)

    #Register resource 
    api.add_resource(TitleQ,    "/v1/title")
    api.add_resource(Title,     "/v1/title/<int:title_id>")

    app.run(port=1337, debug=True, threaded=True)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
