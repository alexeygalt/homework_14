from flask import Flask

from routs.view import title_blueprint, age_blueprint, rating_blueprint, genre_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(title_blueprint)
app.register_blueprint(age_blueprint)
app.register_blueprint(rating_blueprint)
app.register_blueprint(genre_blueprint)

if __name__ == '__main__':
    app.run()
