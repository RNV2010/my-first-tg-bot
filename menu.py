from telebot import types


def start():
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton("📖 Расписание", callback_data='rasp_0')

    return markup.add(btn_1)


def rasp_main():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_1 = types.InlineKeyboardButton('😠 Понедельник', callback_data='rasp_1')
    btn_2 = types.InlineKeyboardButton('😒 Вторник', callback_data='rasp_2')
    btn_3 = types.InlineKeyboardButton('🙄 Среда', callback_data='rasp_3')
    btn_4 = types.InlineKeyboardButton('😏 Четверг', callback_data='rasp_4')
    btn_5 = types.InlineKeyboardButton('😊 Пятница', callback_data='rasp_5')
    btn_6 = types.InlineKeyboardButton("🔙 Назад", callback_data='main')
    return markup.add(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6)


def back_rasp():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_1 = types.InlineKeyboardButton("🔙 Назад", callback_data='rasp_0')
    return markup.add(btn_1)


def back():
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton("🔙 Назад", callback_data='main')
    return markup.add(btn_1)
