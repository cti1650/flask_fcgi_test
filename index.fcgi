#!../../../.linuxbrew/bin/python3.9
from flup.server.fcgi import WSGIServer
from hello import app

if __name__ == '__main__':
    WSGIServer(app).run()