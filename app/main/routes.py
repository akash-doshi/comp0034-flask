from flask import render_template, Blueprint, url_for, request, flash, redirect
from app.main.forms import signupForm

bp_main = Blueprint('main', __name__)



@bp_main.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = signupForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Signup requested for {}'.format(form.name.data))
        # Code to add the student to the database goes here
        return redirect(url_for('main.index'))
    return render_template('signup.html', form=form)
