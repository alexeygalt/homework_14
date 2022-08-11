import sqlite3


def get_actors(actor_one: str, actor_two: str) -> list:
    """Получение списка актеров, играющих с actor_one и actor_two
    в двух или более фильмах"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                    SELECT DISTINCT "cast"
                    FROM netflix
                    WHERE "cast" LIKE '%{actor_one}%' AND "cast" LIKE '%{actor_two}%'        
                    """
        all_actors = []
        for row in cursor.execute(query):
            key = row[0].split(', ')
            all_actors.extend(key)

        result_one = set(filter(lambda x: all_actors.count(x) > 2, all_actors))
        end_result = [item for item in result_one if item != actor_one and item != actor_two]
        return end_result


def get_films_by_options(type_film: str, year: int, genre: str) -> list:
    """Получение фильма/фильмов по указанному типу, году и жанру"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                    SELECT title, description 
                    FROM netflix
                    WHERE "type" = '{type_film}' AND release_year = '{year}' and description LIKE '%{genre}%'
                    
                """
        result = [item for item in cursor.execute(query)]
        if result:
            return result
        return 'По выбранным параметрам нет фильмов'
