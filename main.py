import os

import telebot

import func
import key
import menu
import txt

bot = telebot.TeleBot(key.tgkey, 'html')


def main():
    @bot.message_handler(['start'])
    def com_start(message):
        u_data = [message.from_user.id, message.message_id]
        if message.text == '/start':
            bot.send_message(u_data[0], 'Привет!', reply_markup=menu.start())

    @bot.message_handler(content_types=['text'])
    def text_process(message):
        bot.send_message(message.chat.id, txt.input_message)

    @bot.message_handler(content_types=['document'])
    def excel_table(message):
        u_data = [message.from_user.id, message.message_id]
        if u_data[0] in key.admins:
            try:
                file_info = bot.get_file(message.document.file_id)
                download = bot.download_file(file_info.file_path)
                if os.path.exists('Расписание.xlsx'):
                    os.remove('Расписание.xlsx')
                file_path = os.path.join('Расписание.xlsx')
                #Сохранение файла
                with open(file_path, 'wb') as new_file:
                    new_file.write(download)
                bot.send_message(u_data[0], 'Расписание загруженоб обработка')
                if func.rasp_update(file_path):
                    bot.edit_message_text('Расписание успешно загружено', u_data[0], u_data[1] + 1,
                                          reply_markup=menu.back())
            except Exception:
                bot.send_message(u_data[0], 'Не удалось обработать файл ', reply_markup=menu.back())

    @bot.callback_query_handler(lambda call: True)
    def call_process(call):
        u_data = [call.from_user.id, call.message.message_id]
        if 'rasp' in call.data:
            day_week = func.today()
            if 'rasp_0' == call.data:
                bot.edit_message_text(txt.send_rasp(func.rasp_export(day_week[0]), day_week[1]), u_data[0], u_data[1],
                                      reply_markup=menu.rasp_main())
            elif 'rasp_1' == call.data:
                bot.edit_message_text(txt.send_rasp(func.rasp_export(1), 'Понедельник'), u_data[0], u_data[1],
                                      reply_markup=menu.back_rasp())
            elif 'rasp_2' == call.data:
                bot.edit_message_text(txt.send_rasp(func.rasp_export(2), 'Вторник'), u_data[0], u_data[1],
                                      reply_markup=menu.back_rasp())
            elif 'rasp_3' == call.data:
                bot.edit_message_text(txt.send_rasp(func.rasp_export(3), 'Среда'), u_data[0], u_data[1],
                                      reply_markup=menu.back_rasp())
            elif 'rasp_4' == call.data:
                bot.edit_message_text(txt.send_rasp(func.rasp_export(4), 'Четверг'), u_data[0], u_data[1],
                                      reply_markup=menu.back_rasp())
            elif 'rasp_5' == call.data:
                bot.edit_message_text(txt.send_rasp(func.rasp_export(5), 'Пятница'), u_data[0], u_data[1],
                                      reply_markup=menu.back_rasp())
        elif call.data == 'main':
            bot.edit_message_text('Главное меню', u_data[0], u_data[1], reply_markup=menu.start())


    bot.polling(none_stop=True)







if __name__ == '__main__':
    main()
