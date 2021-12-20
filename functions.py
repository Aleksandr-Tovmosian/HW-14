import sqlite3
from flask import Flask, render_template, request

# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------





title_srch = input()

with sqlite3.connect('netflix.db') as con:
    cur = con.cursor()
    sqlite_query = f'''
                        SELECT title, country, release_year, listed_in, description
                        FROM netflix
                        WHERE "title" LIKE "%{title_srch}%"
                        '''

    cur.execute(sqlite_query)
    res = cur.fetchall()

if len(res) > 1:
    copy_res = res
    year = 0
    count = -1
    for i in copy_res:
        count += 1
        if year < int(i[2]):
            position = count
            year = int(i[2])

    res = copy_res[position]

final_res = {
            "title": res[0],
            "country": res[1],
            "release_year": res[2],
            "genre": res[3],
            "description": res[4].strip(),
            }

if __name__ == '__main__':
    print(final_res)
