import pymongo
from bson import json_util, ObjectId
import json


def update_rank(data: dict) -> bool:
    client = pymongo.MongoClient(host='localhost', port=27017)

    try:
        print(data)
        db = client.snk
        db.drop_collection('rank') #清空
        db.rank.insert_one(data)
        print(data)
        print('ok')
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        client.close()

def get_rank() -> str:
    client = pymongo.MongoClient(host='localhost', port=27017)
    try:
        db = client.snk
        data = db.rank.find_one()
        del data['_id']
        # data = json.dumps(json_util.dumps(data))
        # data = json.dumps(data, indent=4, default=json_util.default)
        data = json.dumps(data)
        print(data)
        return data
    except Exception as e:
        print(e)
        return None
    finally:
        client.close()



if __name__ == '__main__':
    # data = {'1': {'name': 'zs', 'bonus': 1000},
    #         '2': {'name': 'hl', 'bonus': 2000}}
    # update_rank(data)

    get_rank()