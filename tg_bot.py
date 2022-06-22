import logging
import os
import traceback

import dialogflow_api
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (CallbackContext, CommandHandler, Filters,
                          MessageHandler, Updater)


def start(update: Update, context: CallbackContext):
    update.message.reply_markdown_v2('Здравствуйте')


def answer(update: Update, context: CallbackContext):
    is_fallback, intent_text = dialogflow_api.detect_intent_text(
        project_id=os.environ['DIALOGFLOW_PROJECT_ID'],
        session_id=os.environ['DIALOGFLOW_SESSION_ID'],
        text=update.message.text,
        language_code='ru_RU'
        )
    update.message.reply_text(intent_text)


def error_handler(update: object, context: CallbackContext):
    logging.error(traceback.format_exc())
    message = f'TG bot crushed with exception:\n{traceback.format_exc()}'
    context.bot.send_message(
        chat_id=os.environ['TELEGRAM_CHAT_ID'], text=message)


if __name__ == '__main__':
    logging.basicConfig(
        filename='tg_bot.log',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.ERROR
        )
    load_dotenv()
    tg_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    updater = Updater(tg_bot_token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, answer))
    dispatcher.add_error_handler(error_handler)
    updater.start_polling()
    updater.idle()
