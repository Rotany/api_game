from pymongo import MongoClient, errors
import logging

class MongoManager:
    def __init__(self, host, port, database):
        self.logger = logging.getLogger("mongo")
        self.host = host
        self.port = int(port)
        self.mongo_connection = self.__create_connection()
        self.mongo_db = self.mongo_connection[database]

    
    def __create_connection(self):
        try:
            client = MongoClient(host=self.host, port=self.port)
            client.server_info()
            return client
        except errors.ConnectionFailure as e:
            self.logger.exception(f"Could not connect to MongoDB server - {e}")
            raise

    def insert_document(self, collection, data):
        try:
            result = self.mongo_db[collection].insert_one(data)
            return result.inserted_id
        except Exception as e:
            self.logger.exception(f"Could not insert this document")
            raise e
    
    def remove_document(self, collection, filter):
        self.mongo_db[collection].remove(filter)
    
    def create_or_update_document(self, collection, filter, data):
        result = self.mongo_db[collection].update_one(filter=filter, data=data, upsert=True)
        return result.upserted_id or result.modified_count
    
    def list_documents(self, collection, query, find_one, sort_by=None):
        collection = self.mongo_db[collection]
        if find_one:
            return collection.find_one(query)
        if sort_by:
            return collection.find(query).sort(sort_by)
        else:
            return collection.find(query)

    def __list_documents_with_pipeline(self, collection, pipeline):
        return self.mongo_db[collection].aggregate(pipeline)

    def list_best_scores(self, limit=5):
        pipeline = [
            {
                "$lookup": {
                    "from": "users",
                    "localField": "user_id",
                    "foreignField": "_id",
                    "as": "user"
                }
            },
            {
                "$sort": {"score": -1},
            },
            {
                "$limit": limit
            },
            {
                "$project": {
                    "score": 1,
                    "user": {"$arrayElemAt": ["$user", 0]},
                }
            }
        ]
        return self.__list_documents_with_pipeline("final_scores", pipeline)

    def list_points(self,email, limit=10):
        pipeline = [
            {
                "$lookup": {
                    "from": "users",
                    "localField": "user_id",
                    "foreignField": "_id",
                    "as": "user"
                }
            },
            {
             "$match": {
                "user.email": email  # Filtrar por user_id
             }
            },
            {
                "$limit": limit
            },
            {
                "$sort": {"coins": -1, "level": -1, "hearts": -1, "time": -1}
            },
            {
                "$project": {
                    "hearts": 1,
                    "coins": 1,
                    "level": 1,
                    "time": 1,
                    "user": {"$arrayElemAt": ["$user", 0]},
                }
            }
        ]
        return self.__list_documents_with_pipeline("points", pipeline)
    
    def validar_usuario(self, usuario, contrasena):
        # Buscar el usuario en la base de datos
        usuario_encontrado = self.mongo_db['users'].find_one({'email': usuario})
        if usuario_encontrado:
            # Verificar la contraseña
            if usuario_encontrado['password'] == contrasena:
                # Si las contraseñas coinciden, devolver el usuario encontrado
                return True
        # Si el usuario no existe o la contraseña no coincide, devolver None
        return False