from flask import Blueprint, render_template
from ..forms import QuestionForm
from pybo.models import Question

bp = Blueprint('question', __name__, url_prefix='/question')

# /question/list/
@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

# /question/list/detail/<int:question_id>/
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)

# http://127.0.0.1:5000/question/create
@bp.route('/create/')
def create():
    form = QuestionForm()
    return render_template('question/question_form.html', form=form)