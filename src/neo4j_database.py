from neo4j import GraphDatabase, Session, basic_auth
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
                                 "WHERE (any(prop in keys(m) WHERE toString(m[prop]) =~ {keywords})) "
                                 "RETURN m as nod, ID(m) as ck "
                                 "LIMIT {limit}", {"keywords": "(?i).*\\b" + keywords + "\\b.*", "limit": limit})
            # pointer of result
            return self.nodeToJson(result)

    def getNeighbourhood(self, ck):
        with self.driver.session() as session:
            result = session.run("MATCH (m)-[]-(n)"
                                 "WHERE toString(ID(m)) = {ck}"
                                 "return m,n", {"ck": ck})
            return self.nodeToJson(result)

    @staticmethod
    def neibourToJson(result):
        all_nodeJson = []
        for node in result:
            node_json_dict = {}
            for i, j in node.value().items():
                node_json_dict.update({i: j})
            all_nodeJson.append(node_json_dict)
        return dumps(all_nodeJson, indent=2)

    @staticmethod
    def nodeToJson(result):
        all_node_json = []
        for record in result:
            dic = {}
            for i in record.keys():
                if i == 'ck':
                    dic.update({i: record[i]})
                else:
                    for j, k in record[i].items():
                        dic.update({j: k})
            all_node_json.append(dic)
        return dumps(all_node_json)
