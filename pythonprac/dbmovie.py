from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.x6y4kbq.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

db.movies.update_one({'title':'문재인입니다'},{'$set':{'rate':'0.0'}})