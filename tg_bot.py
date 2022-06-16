import logging
import os

from dotenv import load_dotenv
from google.cloud import dialogflow
from telegram import Update
from telegram.ext import (Application, CommandHandler, ContextTypes,
                          MessageHandler, filters)


def detect_intent_text(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
        )
    return response.query_result.fulfillment_text


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Здравствуйте')


async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    intent = detect_intent_text(project_id=os.environ['DIALOGFLOW_PROJECT_ID'],
                                session_id=os.environ['DIALOGFLOW_SESSION_ID'],
                                text=update.message.text,
                                language_code='ru_RU')
    await update.message.reply_text(intent)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
        )
    logger = logging.getLogger(__name__)
    load_dotenv()
    tg_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    application = Application.builder().token(tg_bot_token).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, answer))
    application.run_polling()
