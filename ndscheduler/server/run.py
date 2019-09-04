from tornado_swagger.setup import setup_swagger
import tornado.web
import tornado.ioloop

class PostsDetailsHandler(tornado.web.RequestHandler):
    def get(self, posts_id):
        """
        ---
        # write swagger specification here
        """
        return 'HI'


class Application(tornado.web.Application):
    _routes = [
        tornado.web.url(r'/api/posts', PostsDetailsHandler),

    ]

    def __init__(self):
        setup_swagger(self._routes)
        super(Application, self).__init__(self._routes)


if __name__ == '__main__':
    app = Application()
    app.listen(6666)
    tornado.ioloop.IOLoop.current().start()
