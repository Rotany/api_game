from pymongo import MongoClient

class MongoManager:
    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.mongo_connection = self.__create_connection(host, port)
        self.mongo_db = self.mongo_connection[database]

    
    def __create_connection(self, host, port):
        return MongoClient(host, port)

    def insert_document(self, collection, data):
        self.mongo_db[collection].insert_one(data)
    
    def remove_document(self, collection, filter):
        self.mongo_db[collection].remove(filter)
    
    def list_documents(self, collection, query):
        self.mongo_db[collection].find(query)


