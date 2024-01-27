#!../../../.linuxbrew/bin/python3.9
from wsgiref.handlers import CGIHandler
from hello import app

CGIHandler().run(app)