input_message = '''
Бот не обрабатывает текстовые сообщения
'''


def send_rasp(data_lesson: tuple, day_of_week: str) -> str:
    result = f'<b>Расписание на {day_of_week.lower()}</b> \n'

    for i in data_lesson:
        result = result + f'\n{i[2]}. {i[3]}'
    return result

