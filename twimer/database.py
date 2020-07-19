import pymongo
from pprint import pprint


class MongoDB:
    
    def __init__(self, mongo_url: str):
        self.client = pymongo.MongoClient(mongo_url)
        self.database = self.client.database_tweet
        self.collection = self.database.collection_tweet
        self.admin = self.client.admin

    def insert_one(self, tweet: dict):
        self.collection.insert_one(tweet)

    def get_db_status(self):
        return self.admin.command('serverStatus')
