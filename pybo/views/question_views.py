

from flask import Blueprint, render_template, request, url_for
from ..forms import QuestionForm, AnswerForm
from pybo.models import Question
from werkzeug.utils import redirect
from datetime import datetime
from .. import db

bp = Blueprint('question', __name__, url_prefix='/question')

# /question/list/
@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

# /question/list/detail/<int:question_id>/
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

# http://127.0.0.1:5000/question/create
@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form=form)