# tornado-uvloop
super simple uvloop class for tornado framework


## Usage


```python

import tornado.ioloop
import tornado.web

from tornadouvloop import TornadoUvloop


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Application Running on http://localhost:8888")
    tornado.ioloop.IOLoop.configure(TornadoUvloop)
    tornado.ioloop.IOLoop.current().start()

```