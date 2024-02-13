from flask import Flask
from route import test

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.register_blueprint(test.bp)

if __name__ == "__main__":
  app.run()