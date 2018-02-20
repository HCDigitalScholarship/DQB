from pymongo import MongoClient

client = MongoClient()
db = client['dqb_database']
collection = db['dqb_collection']

def get(key,term):
    # Convert from string to ObjectId:
    document = collection.find_one({ key : term})
    print(document)
    return document

def count(key,term):
	count = collection.find({ key : term}).count()
	print(count)
	return count

def search(key,term):
	result = collection.find({ key : term})
	for stuff in result:
		print(stuff)	
	return result

get('file','DQB_ECCLES-EDRIDGE_Page_080.jpg.jpg')
print("Hello!")

