from flask import Blueprint, request, jsonify

from sql_utils_for_routs import get_title, get_age_film, get_rating_film, get_genre_film

title_blueprint = Blueprint('title_blueprint', __name__)


# поиск по названию фильма
@title_blueprint.route('/movie/<title>')
def get_title_page(title):
    return jsonify(get_title(title))


age_blueprint = Blueprint('age_blueprint', __name__)


# вывод списка фильмов по заданному диапазону
@age_blueprint.route('/movie/<int:year_start>/to/<int:year_end>')
def get_age_film_page(year_start, year_end):
    result = get_age_film(year_start, year_end)
    return jsonify(result)


rating_blueprint = Blueprint('rating_blueprint', __name__)


# вывод списка фильмов по заданному рейтингу
@rating_blueprint.route('/rating/<key>')
def get_rating_page(key):
    if key == 'children':
        return jsonify(get_rating_film(['G']))
    elif key == 'family':
        return jsonify(get_rating_film(['G', 'PG', 'PG-13']))
    elif key == 'adult':
        return jsonify(get_rating_film(['R', 'NC-17']))


genre_blueprint = Blueprint('genre_blueprint', __name__)


@genre_blueprint.route('/genre/<genre>')
def get_genre_page(genre):
    return jsonify(get_genre_film(genre))
