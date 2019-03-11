from neo4j_database import Neo4jDatabase
from json import dumps
from flask import Flask, g, request, Response, render_template

uri = "bolt://10.77.110.133:7687"
user = "neo4j"
password = "slm"

app = Flask(__name__)

db = Neo4jDatabase(uri=uri, user=user, password=password)


@app.teardown_appcontext
def close_db(error):
    db.close();


@app.route("/")
def get_index():
    return render_template('index.html')

@app.route("/searchnode")
def get_graph(self):
    try:
        q = request.args["q"]
    except KeyError:
        return []
    else:
        return Response(db.getRelatedNode(keywords=q))


if __name__ == '__main__':
    app.run(port=8080, debug=True)
