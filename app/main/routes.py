from flask import render_template, Blueprint, url_for, request, flash, redirect
from app.main.forms import signupForm, searchForm
from app import db
from sqlalchemy.exc import IntegrityError
from app.models import User, City, Forecast


bp_main = Blueprint('main', __name__)

@bp_main.route('/', methods=['GET', 'POST'])
@bp_main.route('/home', methods=['GET', 'POST'])
def index():
    form = searchForm()
    cities = City.query.all()
    forecasts = Forecast.query.all()
    print(cities)
    if form.validate_on_submit():
        for city in cities:
            if form.city.data == city.city:
                cityID=city.city_id
                for forecast in forecasts:
                    if forecast.city_id == cityID:
                        flash(f'The forecast for {city.city} is {forecast.forecast}. Written on the {forecast.forecast_datetime}')

        return redirect(url_for('index'))
    return render_template('index.html', cities=cities, forecasts=forecasts, form=form)


@bp_main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = signupForm()
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, email=form.email.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('You have registered as a user.')
        except IntegrityError:
            db.session.rollback()
            flash('Cannot register {}.'.format(form.email.data), 'error')
        return redirect(url_for('main.index'))
    return render_template('signup.html', form=form)

@bp_main.route('/user', methods=['GET'])
def users():
    user_list = User.query.all()
    return render_template("user.html", users=user_list)

@bp_main.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        term = request.form['search_term']
        if term == "":
            flash("Enter a city to search for")
            return redirect('/')
        results = City.query.filter(City.city.contains(term)).all()
        results = City.query.join(Forecast).with_entities(City.city, Forecast.forecast_datetime,Forecast.forecast, Forecast.comment).filter(City.city.contains(term)).all()
        if not results:
            flash("No city found with that name.")
            return redirect('/')
        return render_template('search.html', results=results)
    else:
        return redirect(url_for('main.index'))
