import tornado.ioloop
import tornado.web
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb://user:password@ds261755.mlab.com:61755/catreview')
db = client['catreview']
cats_collection = db['cats']

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cats = list(cats_collection.find())

        self.render("main.html", cats=cats)

class CatHandler(tornado.web.RequestHandler):
    def get(self):
        cat_id = self.get_argument('id')
        cat = cats_collection.find_one({'_id': ObjectId(cat_id)})

        self.render("cat.html", cat=cat)


class AddHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('add.html')

    def post(self):
        name = self.get_argument('name', None)
        photo = self.get_argument('photo', None)
        description = self.get_argument('description', None)

        if name == None or photo == None or description == None:
            self.write('Заполните все поля!')
        else:

            cat = {'name': name, 'photo': photo, 'description': description}
            cats_collection.insert(cat)

            return self.redirect('/')


routes = [
    (r"/", MainHandler),
    (r"/add", AddHandler),
    (r"/cat", CatHandler)
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
