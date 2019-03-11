from neo4j import GraphDatabase, Session
from json import dumps


class Neo4jDatabase(object):
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def getRelatedNode(self, keywords, limit=50, key='m'):
        with self._driver.session() as session:
            result = session.run("MATCH (m)"
                                 "WHERE (any(prop in keys(m) WHERE m[prop] =~ {keywords})) "
                                 "RETURN m "
                                 "LIMIT {limit}", {"keywords": "(?i).*" + keywords + ".*", "limit": limit})
            # pointer of result
            return self.nodeToJson(result)

    def getNeighbourhood(self, ck):
        with self._driver.session() as session:
            result = session.run("MATCH (m)-[]-(n)"
                                 "WHERE ID(m) = {ck}"
                                 "return m,n", {"ck": ck})
            return self.nodeToJson(result)

    @staticmethod
    def nodeToJson(result):
        all_nodeJson = []
        for node in result:
            node_json_dict = {}
            for i, j in node.value().items():
                node_json_dict.update({i: j})
            all_nodeJson.append(node_json_dict)
        return dumps(all_nodeJson, indent=2)
