from telebot import types

def start():
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton("Расписание", callback_data='rasp_0')

    return markup.add(btn_1)