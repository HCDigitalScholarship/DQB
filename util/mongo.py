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
	print(result)	
	return result

result = get('file','DQB_ECCLES-EDRIDGE_Page_080.jpg.jpg')
print(result['data']['responses']['textAnnotations'])

#full text
#print(result['data']['responses'][0]['textAnnotations'][0]['description'])
print(result['data']['responses'][0]['fullTextAnnotation']['text'])

#all word results
for text in result['data']['responses'][0]['textAnnotations']:
    print(text['description'])
#exclude 0 index    
for text in result['data']['responses'][0]['textAnnotations'][1:]:
    print(text['description'])

print("Hello!")

