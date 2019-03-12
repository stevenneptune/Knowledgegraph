from neo4j_database import Neo4jDatabase
from json import dumps
from flask import Flask, g, request, Response, render_template
from neo4j import GraphDatabase, Session, basic_auth

uri = "bolt://localhost:11001"
user = "neo4j"
password = "password"

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
    try:
        q = request.args["q"]
        print(q)
    except KeyError:
        return []
    else:
        result = db.getRelatedNode(keywords=q)
        #print(result)
        return Response(result)
    return False


@app.route("/relatednode/<node>")
def get_relatednode(node):
    print(node)
    result = db.getNeighbourhood(node)
    print(result)
    return Response(result)



if __name__ == '__main__':
    # test()
    #print(db.getRelatedNode('of'))
    # print(db.getNeighbourhood('1'))
    app.run(port=8080, debug=True)

