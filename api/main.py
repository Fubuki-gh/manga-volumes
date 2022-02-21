import sys
from flask import Flask, redirect
from flask_restful import Api

from endpoints.title import TitleQ, Title

app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():
    return redirect(location="https://google.com", code=301)

#Main
def main(argc: int, argv: list[str]) -> None:

    #Register resource 
    api.add_resource(TitleQ,    "/title")
    api.add_resource(Title,     "/title/<int:title_id>")

    app.run(port=1337, debug=True, threaded=True)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
