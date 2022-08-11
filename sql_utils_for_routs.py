import sqlite3


def get_title(title: str) -> dict:
    """ Получение самого свежего фильма через запрос к базе netflix.db"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                SELECT title, country, release_year, "type", description
                FROM netflix
                WHERE title = '{title}'
                ORDER BY date_added DESC
                LIMIT 1                
                """

        key = [item for item in cursor.execute(query)]

        result = {
            "title": key[0][0],
            "country": key[0][1],
            "release_year": key[0][2],
            "genre": key[0][3],
            "description": key[0][4].strip()
        }
        return result


def get_age_film(start: int, end: int) -> list:
    """ Получение списка фильмов через запрос к базе netflix.db по заданному диапазону"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                        SELECT title, release_year  
                        FROM netflix
                        WHERE release_year >= {start} and release_year <= {end}
                        LIMIT 100               
                        """
        key = [item for item in cursor.execute(query)]
        result = []
        for item in key:
            key_d = {
                "title": item[0],
                "release_year": item[1],
            }
            result.append(key_d)

        return result


def get_rating_film(rating: list) -> list:
    """ Получение  списка фильмов через запрос к базе netflix.db по заданному рейтингу"""
    with sqlite3.connect("netflix.db") as connection:
        # вот тут не знаю как нормально разграничить эти два случая:
        # 1) где имеем кортеж значений и ищем через IN
        # 2) где имеем только одно значение и сравниваем
        cursor = connection.cursor()
        if len(rating) > 1:
            rating = tuple(rating)
            query = f"""
                            SELECT title, rating, description 
                            FROM netflix
                            WHERE rating IN {rating}
                            LIMIT 100               
                            """
        else:
            query = f"""
                        SELECT title, rating, description 
                        FROM netflix
                        WHERE rating = '{rating[0]}'
                        LIMIT 100               
                                        """

        key = [item for item in cursor.execute(query)]
        result = []
        for item in key:
            key_d = {
                "title": item[0],
                "rating": item[1],
                "description": item[2].strip(),
            }
            result.append(key_d)

        return result


def get_genre_film(genre: str) -> list:
    """Получение списка фильмов через запрос к базе netflix.db по ключевому жанру фильма"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                     SELECT title, description 
                     FROM netflix
                     WHERE listed_in LIKE '%{genre}%'
                     ORDER BY release_year DESC
                     LIMIT 10               
                                    """
        key = [item for item in cursor.execute(query)]
        result = []
        for item in key:
            key_d = {
                "title": item[0],
                "description": item[1].strip(),
            }
            result.append(key_d)
        return result
