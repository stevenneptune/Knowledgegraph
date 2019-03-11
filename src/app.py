from flask import Flask, Response,request
from neo4j_database import Neo4jDatabase


class webApp(object):
    _app = None
    _db = None

    def __init__(self, staticUrlPath, db_uri, db_user, db_password):
        self._app = Flask(__name__, static_url_path=staticUrlPath)
        self._db = Neo4jDatabase(uri=db_uri, user=db_user, password=db_password)
        return self._app

    def run(self, port, debug=True):
        self.run(port=port, debug=debug)

    @_app.route("/searchnode")
    def get_graph(self):
        try:
            q = request.args["q"]
        except KeyError:
            return []
        else:
            return Response(self._db.getRelatedNode(keywords=q))
