import pymongo

def update_rank(data: dict) -> bool:
    try:
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client.snk
        rank = db.rank
        rank_id = rank.insert_one(data).inserted_id
        return True
    except:
        return False


