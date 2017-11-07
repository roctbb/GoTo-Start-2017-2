import tornado.ioloop
import tornado.web

from random import choice

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        prizes = ['автомобиль', 'iphone x', 'хромосома', 'корова', 'орущий кот', 'банка с огурцами']

        self.render("main.html", prize=choice(prizes).upper())
routes = [
    (r"/", MainHandler),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()