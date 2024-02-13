from flask import Blueprint

bp = Blueprint('web', __name__, url_prefix="/test")

@bp.get('/data')
def test_data():
  return {"hello": "world"}