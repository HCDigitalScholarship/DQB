#pip install google.cloud, pprint
#pip install lxml==3.6.4
#pip install --upgrade google-api-python-client
#gcloud config set project my-new-default-project
#pip install mysql-connector

import io
import os
import pprint
from lxml import etree
from collections import defaultdict

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud import language
import mysql.connector



cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='ocr')
cnx2 = mysql.connector.connect(user='root', password='',
                               host='127.0.0.1',
                               database='ocr')


cursor = cnx.cursor(buffered=True)
cursor2 = cnx2.cursor(buffered=True)


## VISION API SECTION
# Instantiates a client
#vision_client = vision.Client()
vision_client = vision.Client.from_service_account_json('/Users/ajanco/projects/*.json')

# Instantiates a client
language_client = language.Client()

#this finds the last entry in the database and sets the start of the loop at that file
files_list = []
for fn in os.listdir('/Users/ajanco/projects/dl_ocr/DQB/images/'):

    files_list.append(fn)
files_list.sort()

end = len(files_list) 
#Get filename of last record in the db
query = ("SELECT doc_id, doc_name FROM ocr.documents WHERE doc_id = (SELECT MAX(doc_id) FROM ocr.documents);")
cursor.execute(query)

#This finds the index for the file in the list of filenames 

for doc in cursor:
    get_this = doc[1]
    print doc[1]

try:
    i = files_list.index(get_this)
except (NameError, ValueError):
    i = 1


for file in files_list[i:end]:
    print file
    file_name = "/Users/ajanco/projects/dl_ocr/DQB/images/" + file

    file_name_1 = '"' + str(file) + '"'
    #file_name_2 = str(file_name.split('/', -1)[-1])

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        image = vision_client.image(
            content=content)

        # Performs label detection on the image file
        labels = image.detect_text()

        #!! labels[0] is the whole text, all later list items are individual word tokens
        nlp = '"' + labels[0].description.encode('utf8') + '"'
    
        text_query = ("INSERT ocr.texts (file_name, text) VALUES (%s,%s);" % (file_name_1, nlp)) 
        
        cursor.execute(text_query)
        cnx.commit()
       
