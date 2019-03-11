from neo4j_database import Neo4jDatabase
from json import dumps


def main():
    uri = "bolt://10.77.110.133:7687"
    user = "neo4j"
    password = "slm"
    keywords = "angola"
    db = Neo4jDatabase(uri=uri, user=user, password=password)
    result = db.getRelatedNode(keywords=keywords, limit=100)
    for node in result:
        print(type(node))
        print(node.value())
    #print(result)


if __name__ == '__main__':
    main()
