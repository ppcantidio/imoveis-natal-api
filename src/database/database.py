import pymongo
from bson.objectid import ObjectId
from dynaconf import settings


class Database:
    def __init__(self, collection_name):
        client = pymongo.MongoClient(settings["url_connection"])
        db = client.get_database(settings["db_name"])
        self.collection = db.get_collection(collection_name)

    def get_object_by_uuid(self, uuid):
        where = {"uuid": ObjectId(uuid)}
        result = self.collection.find_one(where)
        self._change_uuid_type(result)
        return result

    def update_objet_by_uuid(self, uuid, object):
        where = {"uuid": ObjectId(uuid)}
        result = self.collection.update_one(where, {"$set": object}, upsert=True)
        self._change_uuid_type(result)
        return result

    def delete_by_uuid(self, uuid):
        where = {"uuid": ObjectId(uuid)}
        self.collection.delete_one(where)

    def _change_uuid_type(self, result) -> None:
        if result.get("uuid"):
            result["uuid"] = str(result["uuid"])
