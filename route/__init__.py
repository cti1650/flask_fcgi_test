from . import health, robots, test

def get_blueprint(app):
  app.register_blueprint(health.bp)
  app.register_blueprint(robots.bp)
  app.register_blueprint(test.bp)