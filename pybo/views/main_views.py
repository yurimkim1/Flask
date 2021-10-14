from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
    # 블루프린트 question내에 _list()함수와 연결된 주소
    # /question/list/로 브라우저 너는 다시 접속해