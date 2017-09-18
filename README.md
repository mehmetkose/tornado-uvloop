# tornado-uvloop
super simple uvloop class for tornado framework

## Installation

pip install tornado-uvloop

## Requirements

* Python 3.5 and above
* Tornado 4.x and above
* Uvloop 0.6 and above

### ** Important **

> Your loop type will be changed. Consider that while using 3rd party modules.

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
