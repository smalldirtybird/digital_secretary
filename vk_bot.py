import logging
import os
import random
import vk_api
from dotenv import load_dotenv
from google.cloud import dialogflow
from vk_api.longpoll import VkLongPoll, VkEventType


def detect_intent_text(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
        )
    return response.query_result.fulfillment_text


def echo(event, vk_api):
    intent = detect_intent_text(project_id=df_project_id,
                                session_id=df_session_id,
                                text=event.text,
                                language_code='ru_RU')
    vk_api.messages.send(
        user_id=event.user_id,
        message=intent,
        random_id=random.randint(1, 1000)
    )


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    logger = logging.getLogger(__name__)
    load_dotenv()
    vk_session = vk_api.VkApi(token=os.environ['VK_GROUP_TOKEN'])
    df_project_id = os.environ['DIALOGFLOW_PROJECT_ID']
    df_session_id = os.environ['DIALOGFLOW_SESSION_ID']
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api)
