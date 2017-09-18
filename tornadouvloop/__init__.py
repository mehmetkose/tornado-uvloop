# super simple uvloop class for tornado framework
# https://github.com/mehmetkose/tornado-uvloop

# Licensed under the DWYW license:
# http://dwyw-license.github.io
# Copyright (c) 2016 Mehmet Kose mehmet.py@gmail.com


import tornado.platform
import uvloop
import asyncio

class TornadoUvloop(tornado.platform.asyncio.BaseAsyncIOLoop):

    def initialize(self, **kwargs):
        loop = uvloop.new_event_loop()
        try:
            super(TornadoUvloop, self).initialize(
                loop, close_loop=True, **kwargs)
        except Exception:
            loop.close()
            raise
