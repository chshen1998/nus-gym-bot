from service import getSlots
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import json

def getData():
    file = open('data.json')
    data = json.load(file)
    return data


def main():
    data = getData()

    updater = Updater(token=data['token'], use_context=True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    def start(update, context):
        textmsg = f'Hello {update.effective_user.first_name}, I am NUS Gym Bot. \nUse "/slots" to view available gym slots in NUS.'
        context.bot.send_message(chat_id=update.effective_chat.id, text=textmsg)

    def slots(update, context):
        title = getSlots(data["driver_path"])
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Available slots: {title}')
        
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

if __name__ == "__main__":
    main()