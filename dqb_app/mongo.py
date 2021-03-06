from sshtunnel import SSHTunnelForwarder
import pymongo
import pprint

MONGO_HOST = '165.82.13.130'
MONGO_DB = 'dqb_database'
MONGO_USER = 'digitalscholarship'
MONGO_PASS = 'safari77'

server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_username=MONGO_USER,
    ssh_password=MONGO_PASS,
    remote_bind_address=('127.0.0.1', 27017)
)

server.start()

client = pymongo.MongoClient('127.0.0.1', server.local_bind_port) # server.local_bind_port is assigned local port
db = client[MONGO_DB]
pprint.pprint(db.collection_names())

server.stop()
