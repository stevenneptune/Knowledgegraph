from neo4j_database import Neo4jDatabase
from json import dumps
from flask import Flask, g, request, Response, render_template
from neo4j import GraphDatabase, Session, basic_auth

uri = "bolt://10.77.110.133:7687"
user = "neo4j"
password = "slm"

app = Flask(__name__)

db = Neo4jDatabase(uri, user, password)

def get_db():
    return db


@app.teardown_appcontext
def close_db(error):
    db.close();


@app.route("/")
def get_index():
    return render_template('index.html')


@app.route("/searchnode")
def get_graph():
    neo4j = get_db()
    try:
        q = request.args["q"]
        print(q)
    except KeyError:
        return []
    else:
        print(db.getRelatedNode(keywords=q))
        return Response(db.getRelatedNode(keywords=q))
    return False


if __name__ == '__main__':
    # test()
    app.run(port=8080, debug=True)
