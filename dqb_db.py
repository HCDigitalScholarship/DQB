from pymongo import MongoClient

client = MongoClient()
db = client['dqb_database']
collection = db['dqb_collection']

def get(key,term):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({ key: term})

def count(key,term):
	collection.find({key : term}).count()


def search(key,term):
	result = collection.find({key : term})
	print(result.value())


