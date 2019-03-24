from neo4j import GraphDatabase, Session, basic_auth, BoltStatementResult, BoltStatementResultSummary
from json import dumps
import time


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
                                 # "LIMIT {limit}",
                                 , {"keywords": "(?i).*\\b" + str.strip(keywords) + "\\b.*"})
            # pointer of result
            # print(self.nodeToJson(result))

            return result

    def getNeighbourhood(self, ck):
        #print(type(ck))
        with self.driver.session() as session:
            result = session.run("MATCH (m)-[r]-(n)"
                                 "WHERE ID(m) = {ck}"
                                 "return m as start,n as end,r as relationship", {"ck": int(ck)})
            return result

    @staticmethod
    def neibourToJson(result):
        relationships = result.graph().relationships
        relationlist = {}
        index = 0
        nodes = []
        edges = []
        for eachRel in relationships:
            startcaption = ""
            endcaption = ""
            if index == 0:
                for i, j in eachRel.end_node.items():
                    startcaption += i + ":" + str(j) + "\n"
                nodes.append({'id': index, 'caption': startcaption})
                index += 1
                for i, j in eachRel.start_node.items():
                    endcaption += (i + ":" + str(j) + "\n")
                nodes.append({'id': index, 'caption': endcaption})
                edgeLabel = eachRel.type
                edges.append({'source': 0, 'target': 1, 'caption': edgeLabel})
            else:
                for i, j in eachRel.start_node.items():
                    endcaption += (i + ":" + str(j) + "\n")
                nodes.append({'id': index, 'caption': endcaption})
                index += 1
                edgeLabel = eachRel.type
                edges.append({'source': 0, 'target': index, 'caption': edgeLabel})
        relationlist.update({'nodes': nodes})
        relationlist.update({'links': edges})
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

    def getNodeTime(self, keywords):
        total_time = 0.0
        start = time.time()
        result = self.getRelatedNode(keywords)
        total_time = time.time() - start
        return total_time

    def getNeiTime(self, ck):
        total_time = 0.0
        start = time.time()
        result = self.getNeighbourhood(ck)
        total_time = time.time() - start
        return total_time
