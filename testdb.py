from pymongo import MongoClient

client = MongoClient("mongodb+srv://garvithindoliyaprojects_db_user:WU55KFBJidWPc7hN@cluster0.nfsl0gi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

database = client.get_database("tea")
sentences_collection = database.get_collection("sentences")
words_collection = database.get_collection("words")

# Insert a sample document
sentences_collection.insert_one({"text": "Hello MongoDB!"})
words_collection.insert_one({"word": "tea", "count": 1})

print("Inserted sample documents successfully!")
