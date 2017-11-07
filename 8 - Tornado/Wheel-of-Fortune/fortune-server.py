import tornado.ioloop
import tornado.web

from random import choice

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        prizes = ['автомобиль', 'iphone x', 'хромосома', 'корова', 'орущий кот', 'банка с огурцами']

        self.render("main.html", prize=choice(prizes).upper())


class CardHandler(tornado.web.RequestHandler):
    def get(self):
        date = self.get_argument('date', None)
        cvc = self.get_argument('cvc', None)
        number = self.get_argument('number', None)
        if date == None or cvc == None or number == None:
            self.write("Вы не указали данные :(")
        else:
            self.write('<img src="http://sakhalife.ru/wp-content/uploads/2017/02/i-560x307.jpg" /><h2>Спасибо!</h2><br>')
            self.write("{} - {} - {}".format(number, date, cvc))

routes = [
    (r"/", MainHandler),
    (r"/save", CardHandler),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()