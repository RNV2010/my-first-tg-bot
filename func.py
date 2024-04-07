import datetime
import sqlite3

import openpyxl

import key

time_now = lambda: datetime.datetime.now().strftime("%Y/%m/%d %H:%M")


def today(num_day: int = 0) -> tuple:
    week_days = ['Понедельник', 'Второник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    if num_day == 0:
        day_of_week = datetime.datetime.now().weekday() + 1
    else:
        day_of_week = num_day
    current_day = week_days[day_of_week - 1]
    return day_of_week, current_day


def rasp_export(day_week: int) -> tuple:
    conn = sqlite3.connect(key.db)
    try:

        cur = conn.cursor()
        cur.execute('SELECT * FROM rasp WHERE day_week=?', (day_week,))
        data = cur.fetchall()
        print(data)
        return data
    except Exception as e:
        print('error rasp_import', e)
    finally:
        conn.close()


def rasp_import(day_week: int, num_lesson: int, name_lesson) -> None:
    conn = sqlite3.connect(key.db)
    try:
        cur = conn.cursor()
        cur.execute('INSERT INTO rasp (day_week, num_lesson, name_lesson) VALUES (?, ?, ?)', 
                    (day_week, num_lesson, name_lesson))

    except Exception as e:
        print('error rasp_import', e)
    finally:
        conn.close()


def rasp_update(excel_file: str) -> bool:
    conn = sqlite3.connect(key.db)
    workbook = openpyxl.load_workbook(excel_file)
    try:
        cur = conn.cursor()
        cur.execute('DELETE FROM rasp')
        conn.commit()
        for day_index, day_name in enumerate(['Пн','Вт','Ср','Чт','Пт']):
            worksheet = workbook[day_name]
            for row in worksheet.iter_rows(min_row=2, values_only=True):
                num_lesson, name_lesson = row

                cur.execute('INSERT INTO rasp (day_week, num_lesson, name_lesson) VALUES (?, ?, ?)',
                            (day_index + 1, num_lesson, name_lesson))
        conn.commit()
        return True

    except Exception as e:
        print('error rasp_import', e)
        return False
    finally:
        conn.close()




