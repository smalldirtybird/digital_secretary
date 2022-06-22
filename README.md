# Digital smart secretary

![](https://psv4.userapi.com/c240331/u328907/docs/d48/fb2292df8f5d/secretary_tg_demo.gif?extra=kBiH-uR6-L7BvIZrDYC8OF5df9lKSgV6Bu20GV7H_s2tUJkz3boUYfC2azdw2z2o2AGPQlMqZCT2Fa4I2z7IJHN2qoRpZKsfWc_JYOjBgAcmiyTUlJZDxaJyT7CuoTy4qmdygrw_o2JtoMb0Sg)

This bot will answer frequently asked questions automatically due to neural network learning.
 
## How it works:

Having received a message via [Telegram](https://t.me/SmartSecretaryBot) or [VK](https://vk.com/im?media=&sel=-213965547), the bot will try to answer it automatically, processing it using the [Dialogflow](https://dialogflow.cloud.google.com/) service. In case of failure, the bot will ask you to ask a question more correctly in Telegram, or provide an opportunity to answer the question to the operator in VK.

Examples of working bots are available at the links in the titlesю

## What is [Dialogflow](https://dialogflow.cloud.google.com/)

[Dialogflow](https://dialogflow.cloud.google.com/) is a natural language recognition cloud service. Digital secretary bots interact with it via an API to find answers to frequently asked questions.

## How to prepare:
1. Make sure Python installed on your PC - you can get it from [official website](https://www.python.org/).
   

2. Install libraries with pip:
    ```
    pip3 install -r requirements.txt
    ```

  
3. Create a Telegram bot which will talk with users and send mesages about program errors - just send message `/newbot` to [@BotFather](https://telegram.me/BotFather) and follow instructions.
    After bot will be created, get token from @BotFather and add to .env file:
    ```
    TELEGRAM_BOT_TOKEN ='your_telegram_bot_token'
    ```
    Put your token instead of value in quotes.

   
4. Get Telegram id of user who will receive mesages about program errors - send message `/start` to [@userinfobot](https://telegram.me/userinfobot) and copy value of id from answer.
    Add the string
    ```
    TELEGRAM_CHAT_ID='YourTelegramID'
    ```
    to .env file.
    
   
 5. For [VK](https://vk.com/) bot you should generate VK API token from community page. Proceed to [Managed communities page](https://vk.com/groups?tab=admin), chose your group and on `Manage/API usage` tab generate token by clicking `Generate token` button. Then put the token to /env file:
 ```
 VK_GROUP_TOKEN = 'yor vk_group_token'
 ```
 
 
 7. Now we need to connect the bot to the [Dialogflow](https://dialogflow.cloud.google.com/#/getStarted) to teach it how to answer frequently asked questions.

    7.1 Create account on [Dialogflow](https://dialogflow.cloud.google.com/#/getStarted) 

    7.2 Create project following [instructions](https://cloud.google.com/dialogflow/es/docs/quick/setup). Then copy ProjecID from [dashboard tab](https://console.cloud.google.com/home/) and put it to .env file:
    ```
    DIALOGFLOW_PROJECT_ID = 'your_project_id'
    ```
    
    7.3 Create an agent folowing [instruction](https://cloud.google.com/dialogflow/es/docs/quick/build-agent)
    
    7.4 Following [instructions](https://cloud.google.com/docs/authentication/getting-started) download JSON key file, copy filepath and add it to .env file:
    ```
    GOOGLE_APPLICATION_CREDENTIALS = 'json_key_filepath'
    ```
    
    7.5 Finally, add variable `DIALOGFLOW_SESSION_ID` to .env file. It can be any combination of numbers, Telegram chat id is perfect for this.
 

## How to run:

Bot can be launched from the terminal with the commands:

Telegram bot:`$ python3 tg_bot.py`

VK bot: `$ python3 vg_bot.py`
