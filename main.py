from flask import Flask, send_from_directory, request
from route import get_blueprint

app = Flask(__name__, static_folder='static')

@app.route('/')
def hello_world():
    return {"hello": "world"}

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

get_blueprint(app)

if __name__ == "__main__":
  app.run()