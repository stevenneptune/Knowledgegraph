import vertica_python
from vertica_database import VerticaDatabase

host = '10.77.110.133'
user = 'dbadmin'
password = 'slm'
database = 'ldbc'

db = VerticaDatabase(host=host, user=user, password=password, database=database)


def main():
    # #hf_key_list = ["china", "love", "see", "know", "came", "project", "say", "work", "people", "money"]
    # lf_key_list = ["pillar", "cargo", "spider", "fork", "velocity", "boost", "welcome", "pony", "honey", "scholarship"]
    #
    # #for i in hf_key_list:
    # #   print(db.getNodeTime(keywords=i))
    #
    # print("lf")
    # for i in lf_key_list:
    #     print(db.getNodeTime(keywords=i))
    # # print(db.getNodeTime("china"))
    result = db.getNeighbourhood(ck=3300240518237635)
    print(result)
    result = result[0]
    for i in result:
        if result[i] != None :
            print(i,result[i])


if __name__ == '__main__':
    main()
