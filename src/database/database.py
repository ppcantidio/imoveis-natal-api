import pymongo
from bson.objectid import ObjectId
from dynaconf import settings


class Database:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        client = pymongo.MongoClient(settings["URL_CONNECTION"])
        db = client.get_database(settings["DB_NAME"])
        self.collection = db.get_collection(self.collection_name)

    def insert_object(self, object):
        self.collection.insert_one(object)

    def get_object_by_uuid(self, uuid):
        where = {"_id": ObjectId(uuid)}
        result = self.collection.find_one(where)
        self._change_uuid_type(result)
        return result

    def update_objet_by_uuid(self, uuid, object):
        where = {"_id": ObjectId(uuid)}
        result = self.collection.update_one(where, {"$set": object}, upsert=True)
        self._change_uuid_type(result)
        return result

    def delete_by_uuid(self, uuid):
        where = {"_id": ObjectId(uuid)}
        self.collection.delete_one(where)

    def _change_uuid_type(self, result) -> None:
        if result is not None:
            result["_id"] = str(result["_id"])
