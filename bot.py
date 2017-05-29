import telepot
import time


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        command = msg['text']
        print('Command Received : {}'.format(command))
        if '/oi' == command:
            bot.sendMessage(chat_id, "Hello how are you?")
        if '/1' == command:
            bot.sendMessage(chat_id, 'Ok be working')

bot = telepot.Bot('313706502:AAHJvKb0hRk-U5B6YFzLTuYIByr5EFwHSWQ')  # Create a bot with key telegram
bot.message_loop(handle)  # Adds the handle function to be called whenever a new message is received

while 1:
    time.sleep(100)