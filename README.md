# Digital smart secretary

This bot will answer frequently asked questions automatically due to neural network learning.
 
## How to prepare:
1. Make sure Python installed on your PC - you can get it from [official website](https://www.python.org/).
   

2. Install libraries with pip:
    ```
    pip3 install -r requirements.txt
   ```
   
3. Create a Telegram bot which will answer to questions - just send message `/newbot` to [@BotFather](https://telegram.me/BotFather) and follow instructions.
    After bot will be created, get token from @BotFather and add to .env file in directory with main.py file(use Notepad++):
    ```
    TELEGRAM_BOT_TOKEN ='your_telegram_bot_token'
    ```
    Put your token instead of value in quotes.

4. Add to .env file string looks like
    ```
   DIALOGFLOW_SESSION_ID = 'session_id'
   ```
   where 'session_id' - arbitrary numeric value as which you can use your Telegram user ID. Just write `/start` to [@getmyid_bot](https://telegram.me/getmyid_bot)


## How to use:
Run `main.py` with console. Use `cd` command if you need to change directory:
```
D:\>cd D:\learning\python\Chat_bots\devman_review_notifier
D:\learning\python\Chat_bots\devman_review_notifier>python main.py
```