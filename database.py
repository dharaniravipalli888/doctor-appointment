from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["user_database"]
users_collection = db["users"]
applications_collection = db["applications"]  