import telebot
import key
import menu
import txt

bot = telebot.TeleBot(key.tgkey, 'html')


def main():
    @bot.message_handler(['start'])
    def com_start(message):
        if message.text == '/start':
            bot.send_message(message.chat.id, 'Привет!', reply_markup=menu.start())


    @bot.callback_query_handler(lambda call: True)
    def call_process(call):
        u_data = [call.from_user.id, call.message.message_id]
        if call.data == 'rasp_0':
            bot.edit_message_text('Расписание', u_data[0], u_data[1])

    bot.polling(none_stop=True)


    @bot.message_handler(content_types= ['text'])
    def text_process(message):
        bot.send_message(message.chat.id, txt.input_message)







if __name__ == '__main__':
    main()
