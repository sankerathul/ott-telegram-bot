import os
import dotenv
import telebot

dotenv.load_dotenv()

BOT_API_KEY = os.getenv('BOT_API_KEY')

bot = telebot.TeleBot(BOT_API_KEY)


@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, "OTT Hunter Coming Soon\nStay Tuned")

bot.polling()