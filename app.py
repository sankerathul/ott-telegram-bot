import os
import dotenv
import telebot
import logging

dotenv.load_dotenv()

BOT_API_KEY = os.getenv('BOT_API_KEY')

bot = telebot.TeleBot(BOT_API_KEY)

logging.basicConfig(filename="app.log", level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filemode="w")

logging.info(f'[INFO] BOT Server Started')

@bot.message_handler()
def start(message):
    logging.info(f'[INFO] Message Received --> {message.chat.id} : {message.text}')
    bot.send_message(message.chat.id, "OTT Hunter Coming Soon\nStay Tuned")

bot.polling()