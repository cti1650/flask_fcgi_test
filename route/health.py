from flask import Blueprint

bp = Blueprint('health', __name__, url_prefix="/")

@bp.get('/healthcheck')
def health_check():
  return "ok"