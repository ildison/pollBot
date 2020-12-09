from datetime import datetime, time
from os import environ
from telegram.ext import Updater

token = environ["TOKEN"]
chat_id = environ["TESTGROUPID"]

updater = Updater(token=token)

def poller(context):
    bot = context.bot
    today = datetime.now().strftime("%d.%m")
    question = f"Футбол. {today}"
    try:
        bot.send_poll(chat_id=chat_id, question=question, options=["+", "-"], is_anonymous=False)
    except Exception as error:
        print(error)

time = time(18,44,40, 0000)
updater.dispatcher.job_queue.run_daily(poller, time, days=(0,1,2,3,4,5,6))
updater.dispatcher.job_queue.start()
updater.idle()
