from flask import Blueprint, send_from_directory

bp = Blueprint('robots', __name__, static_url_path='/static')

@bp.route('/robots.txt')
def generate_robots():
    return send_from_directory(bp.static_folder, 'robots.txt')