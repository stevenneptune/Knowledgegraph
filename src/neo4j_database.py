from neo4j import GraphDatabase, Session,basic_auth
from json import dumps


class Neo4jDatabase(object):
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=basic_auth(user, password))

    def creatSession(self):
        return self.driver.session()

    def close(self):
        self.driver.session().close()

    def getRelatedNode(self, keywords, limit=50):
        with self.creatSession() as session:
            result = session.run("MATCH (m)"
                                 "WHERE (any(prop in keys(m) WHERE m[prop] =~ {keywords})) "
                                 "RETURN m "
                                 "LIMIT {limit}", {"keywords": "(?i).*" + keywords + ".*", "limit": limit})
            # pointer of result
            return self.nodeToJson(result)

    def getNeighbourhood(self, ck):
        with self.driver.session() as session:
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
