from flask import Flask, render_template, flash, redirect, url_for
from app.main.forms import signupForm
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig

db = SQLAlchemy()


def create_app(config_class=DevConfig):
    """
    Creates an application instance to run using settings from config.py
    :return: A Flask object
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

# Initialise the database and create tables
    db.init_app(app)

    @app.route('/')
    @app.route('/home')
    def index():
        return render_template('index.html')

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        form = signupForm()
        if form.validate_on_submit():
            flash('Success')
            return redirect(url_for('index'))

        return render_template('signup.html', form=form)

    if __name__ == '__main__':
        app.run(debug=True)


        # Register Blueprints
    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app
