import logging
import os
import random
import traceback

import dialogflow_api
import vk_api
from dotenv import load_dotenv
from telegram import Bot
from vk_api.longpoll import VkEventType, VkLongPoll


class TelegramLogsHandler(logging.Handler):

    def __init__(self, bot_token, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = Bot(token=bot_token)

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def answer(event, api):
    is_fallback, intent_text = dialogflow_api.detect_intent_text(
        project_id=os.environ['DIALOGFLOW_PROJECT_ID'],
        session_id=os.environ['DIALOGFLOW_SESSION_ID'],
        text=vk_event.text,
        language_code='ru_RU'
        )
    if not is_fallback:
        api.messages.send(user_id=event.user_id,
                          message=intent_text,
                          random_id=random.randint(1, 1000))


if __name__ == '__main__':
    logging.basicConfig(
        filename='vk_bot.log',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    load_dotenv()
    vk_session = vk_api.VkApi(token=os.environ['VK_GROUP_TOKEN'])
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    logger = logging.getLogger('TelegramLogger')
    logger.addHandler(TelegramLogsHandler(
        os.environ['TELEGRAM_BOT_TOKEN'], os.environ['TELEGRAM_CHAT_ID']))
    while True:
        try:
            for vk_event in longpoll.listen():
                if vk_event.type == VkEventType.MESSAGE_NEW and vk_event.to_me:
                    answer(vk_event, vk_api)
        except Exception as error:
            logging.error(traceback.format_exc())
            logger.error(
                f'VK bot crushed with exception:\n{traceback.format_exc()}')
