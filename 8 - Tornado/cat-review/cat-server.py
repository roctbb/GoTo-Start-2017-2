import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        with open('cats.json') as f:
            json_cats = f.read()
        cats = json.loads(json_cats)

        self.render("main.html", cats=cats)


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
            with open('cats.json') as f:
                json_cats = f.read()
            cats = json.loads(json_cats)

            cat = {'name': name, 'photo': photo, 'description': description}
            cats.append(cat)

            with open('cats.json', 'w') as f:
                f.write(json.dumps(cats))

            return self.redirect('/')


routes = [
    (r"/", MainHandler),
    (r"/add", AddHandler)
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
