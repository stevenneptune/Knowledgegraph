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
            result = session.run("MATCH (m)-[r]-(n)"
                                 "WHERE toString(ID(m)) = {ck}"
                                 "return m as start,n as end,r as relationship", {"ck": ck})
            return self.neibourToJson(result)

    @staticmethod
    def neibourToJson(result):
        relationships = result.graph().relationships
        relationlist = []
        for eachRel in relationships:
            startnode = {}
            for i, j in eachRel.start_node.items():
                startnode.update({i: j})
            endnode = {}
            for i, j in eachRel.end_node.items():
                endnode.update({i: j})
            label = eachRel.type
            relationlist.append([{'start': startnode}, {'end': endnode}, {'label': label}])
        return dumps(relationlist, indent=2)

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
