import os
from flask import Flask, render_template, flash, redirect, url_for
import grpc

from cinema_library_pb2 import FilmGenre, RecommendationRequest, FilmId
from cinema_library_pb2_grpc import RecommendationsStub

from users_pb2 import Status, UserRequest, RatingRequest, MarksUpdateRequest
from users_pb2_grpc import UsersStub

from app import app
from app.forms import PastebinEntry, LoginForm

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
recommendations_client = RecommendationsStub(recommendations_channel)

users_host = os.getenv("USERS_HOST", "localhost")
users_channel = grpc.insecure_channel(f"{users_host}:50052")
users_client = UsersStub(users_channel)

current_user = None


@app.route("/", methods=['GET'])
@app.route("/index", methods=['GET'])
def index():
    global recommendations_client
    recommendations_request = RecommendationRequest(category=FilmGenre.ALL)
    recommendations_response = recommendations_client.Recommend(recommendations_request)
    return render_template(
        "homepage.html",
        recommendations=recommendations_response.recommendations
    )

@app.route('/film/<id>', methods=['GET', 'POST'])
def render_film(id):
    global recommendations_client, users_client, current_user
    film_request = FilmId(id=int(id))
    film = recommendations_client.GetFilm(film_request)
    rating_request = RatingRequest(film_id=int(id))
    rating = users_client.FilmRating(rating_request)
    form = PastebinEntry()
    if form.marks.data is not None and current_user is not None:
        marks_update_request = MarksUpdateRequest(
            username=current_user[0],
            mark=int(form.marks.data),
            film_id=int(film.id)
        )
        _ = users_client.UserMarksUpdate(marks_update_request)
    elif form.marks.data is not None:
        flash('Для возможности ставить оценки фильмам необходимо зайти в аккаунт')
    return render_template(
        "film.html",
        film=film,
        form=form,
        rating=f'Средняя оценка {rating.rating}' if rating.rating > 0 else 'Оценок нет'
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    global current_user
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template('login.html', title='Sign In', form=form)
        
    user_request = UserRequest(username=form.username.data, password=form.password.data)
    status = users_client.UserExist(user_request)
    if status.status == Status.EXIST:
        current_user = form.username.data, form.password.data
        flash(f'Вы зашли под именем {form.username.data}')
        return redirect(url_for('index'))
    else:
        flash("Некорректные данные для входа")
    return render_template('login.html', title='Sign In', form=form)

@app.route('/user', methods=['GET'])
def user():
    global current_user
    if current_user is None:
        return redirect(url_for('index'))
    user_request = UserRequest(username=current_user[0], password=current_user[1])
    user_marks_value = users_client.UserMarks(user_request)
    marks = []
    for mark in user_marks_value.marks:
        film_request = FilmId(id=int(mark.film_id))
        film = recommendations_client.GetFilm(film_request)
        marks.append((mark.film_id, mark.mark, film.title))
    return render_template('user.html', user=current_user, marks=marks)
