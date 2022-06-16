import argparse
import json
import os

from dotenv import load_dotenv
from google.cloud import dialogflow


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)
    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)
    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )
    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )


def get_arguments():
    parser = argparse.ArgumentParser(
        description='It\'s a script for upload new intents to Dialogflow.')
    parser.add_argument('-f', '--folder', help='''
                        Input absolute filepath to json with intents, answers and questions.
                        '''
                        )
    parser.add_argument('-in', '--intent_name', help='''
                        Input intent name from json file which should be uploaded to Dialogflow.
                        '''
                        )
    args = parser.parse_args()
    return args.folder, args.intent_name


if __name__ == '__main__':
    load_dotenv()
    file_path, intent_name = get_arguments()
    df_project_id = os.environ['DIALOGFLOW_PROJECT_ID']
    with open(os.path.normpath(file_path), 'r') as questions_json:
        questions_content = json.load(questions_json)
    content = questions_content[intent_name]
    create_intent(project_id=df_project_id,
                  display_name=intent_name,
                  training_phrases_parts=content['questions'],
                  message_texts=[content['answer']]
                  )
