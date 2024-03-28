from . import health, test

def get_blueprint(app):
  app.register_blueprint(health.bp)
  app.register_blueprint(test.bp)