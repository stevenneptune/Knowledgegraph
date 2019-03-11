from flask import Flask, Response, request
from neo4j_database import Neo4jDatabase


class webApp(object):

    def __init__(self, db_uri, db_user, db_password):
        self._app = Flask(__name__,static_url_path='/template/')
        self._db = Neo4jDatabase(uri=db_uri, user=db_user, password=db_password)


    def add_url(self):
        self._app.add_url_rule('/',view_func=self.get_index())
        self._app.add_url_rule('/searchnode', view_func=self.get_graph())

    def run(self, port, debug=True):
        self._app.run(port=port, debug=debug)

    def get_index(self):
        return self._app.send_static_file('index.html')

    def get_graph(self):
        try:
            q = request.args["q"]
        except KeyError:
            return []
        else:
            return Response(self._db.getRelatedNode(keywords=q))
