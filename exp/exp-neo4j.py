from neo4j_database import Neo4jDatabase
import random

uri = "bolt://10.77.110.133:7687"
user = "neo4j"
password = "slm"

db = Neo4jDatabase(uri, user, password)


def main():
    hf_key_list = ["china", "love", "see", "know", "came", "project", "say", "work", "people", "money"]
    lf_key_list = ["pillar", "cargo", "spider", "fork", "velocity", "boost", "welcome", "pony", "honey", "scholarship"]
    result = db.getRelatedNode(keywords="china")
    print(result)
    print("hf")

    for i in hf_key_list:
        print(db.getNodeTime(keywords=i))

    print("lf")
    for j in lf_key_list:
        print(db.getNodeTime(keywords=j))

    print("nei")
    for i in range(100):
        ck = random.randint(0, 3240318)
        print(db.getNeiTime(ck=ck))


if __name__ == '__main__':
    main()
