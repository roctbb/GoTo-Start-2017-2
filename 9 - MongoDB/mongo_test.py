from pymongo import MongoClient

client = MongoClient('mongodb://user:password@ds261755.mlab.com:61755/catreview')
db = client['catreview']
cats_collection = db['cats']

'''
cat = {'name': "Васька",
       'photo': "http://kot-pes.com/wp-content/uploads/2016/09/image4-8-650x433.jpeg",
       'description': "грустный кот :("}

cats_collection.insert(cat)
'''
print(list(cats_collection.find({"name": "Васька"})))
