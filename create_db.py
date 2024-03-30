import sqlite3

'''
таблица с расписанием (rasp)
day_week: int
num_lesson: int
name_lesson: str

'''
conn = sqlite3.connect('database.sqlite3')

try:
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS rasp (
        id INTEGER PRIMARY KEY,
        day_week INTEGER,
        num_lesson INTEGER,
        name_lesson TEXT)''')
    conn.commit()
    print('База данных успешно создана!')
except Exception as e:
    print('не удалось создать базу данных', e)
finally:
    conn.close()
