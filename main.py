from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import logging

updater = Updater(token='1929838326:AAF4GHWsAQyl_U1GQDsiL6GGSDSGxNGJ2dw', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    textmsg = f'Hello {update.effective_user.first_name}, I am NUS Gym Bot. \nUse "/slots" to view available gym slots in NUS.'
    context.bot.send_message(chat_id=update.effective_chat.id, text=textmsg)

def slots(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Available slots:")
    
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, that is not a valid command.")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('slots', slots))
updater.dispatcher.add_handler(CommandHandler('caps', caps))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
updater.idle()