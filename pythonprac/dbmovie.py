from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.x6y4kbq.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

db.movies.delete_one({'title':'말없는 소녀'})