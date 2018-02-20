import os
import googleapiclient.discovery
from tqdm import tqdm

from pymongo import MongoClient
from api_key import VISION_API
import tempfile
from google.cloud import vision
import base64
import io
import pprint
import shutil




API_KEY = VISION_API

client = MongoClient()
db = client['dqb_database']
collection = db['dqb_collection']


def vision_ocr(directory,language):
	
	service = googleapiclient.discovery.build('vision', 'v1', developerKey=API_KEY)
	for file in tqdm(os.listdir(directory)):
		#check if file's already in the db, skip if it's there
		if collection.find_one({'file': file }):
					print("[*] %s already in database" % file)
					pass
		else:
			#open the file, send to Vision API, save to db
			with open(directory + file, 'rb') as image:
				image_content = base64.b64encode(image.read())
				service_request = service.images().annotate(body={
	            	   'requests': [{
	                	   'image': {
	                    	   'content': image_content.decode('UTF-8')
	                      	  },
	                    	'imageContext': {
	                       	 'languageHints': [language]},
	                    	'features': [{
	                       	 'type': 'TEXT_DETECTION'
	                   	 }]
	               	 }]
	           	 })
				response = service_request.execute()
			
				if 'error' in response['responses'][0]:
					print('[*] error %s' % file)
					pass

				else:	
					entry = {}
					entry['file'] = file
					entry['data'] = response
					collection.insert_one(entry)
					#es.index(index="quaker",doc_type="entry",body=entry)
					print('[*] added %s' % file)

					

#pdf_jpg('/home/digitalscholarship/DQB/PDF/')
#clean_jpg('/home/digitalscholarship/DQB/jpg/')
vision_ocr('/srv/DQB/dqb_app/static/jpg/','en')

