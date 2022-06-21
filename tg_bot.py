import logging
import os
import traceback

from dotenv import load_dotenv
from google.cloud import dialogflow
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


def detect_intent_text(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
        )
    return response.query_result.fulfillment_text


def start(update: Update, context: CallbackContext):
    update.message.reply_markdown_v2('Здравствуйте')


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('Help!')


def answer(update: Update, context: CallbackContext):
    intent = detect_intent_text(project_id=os.environ['DIALOGFLOW_PROJECT_ID'],
                                session_id=os.environ['DIALOGFLOW_SESSION_ID'],
                                text=update.message.text,
                                language_code='ru_RU')
    update.message.reply_text(intent)


def error_handler(update: object, context: CallbackContext) -> None:
    logging.error(traceback.format_exc())
    message = f'TG bot crushed with exception:\n{traceback.format_exc()}'
    context.bot.send_message(chat_id=os.environ['TELEGRAM_CHAT_ID'], text=message)


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
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, answer))
    dispatcher.add_error_handler(error_handler)
    updater.start_polling()
    updater.idle()
