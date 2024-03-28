from flask import Flask, send_from_directory
from route import get_bp

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello_world():
    return {"hello": "world"}

get_blueprint(app)

if __name__ == "__main__":
  app.run()