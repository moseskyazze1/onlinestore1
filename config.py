import pymongo
import certifi

con_str = "mongodb+srv://test:test@cluster0.vjnkcty.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("project1")
