from datetime import datetime, time
from os import environ
from telegram.ext import Updater

token = environ["TOKEN"]
chat_id = environ["TESTGROUPID"]

updater = Updater(token=token)
jobQueue = updater.dispatcher.job_queue
pollBot = updater.bot

def unpinMessage(context):
    message_id = context.job.context.message_id
    chat_id = context.job.context.chat_id

    pollBot.unpin_chat_message(chat_id, message_id)
    print("PollBot unpined message")

def pinMessage(message):
    message_id = message.message_id
    chat_id = message.chat_id

    pollBot.pin_chat_message(chat_id, message_id)
    print("PollBot pined message")

def scheduleUnpinningMessage(message):
    jobQueue.run_once(unpinMessage, context=message, when=200)
    print("PollBot scheduled unpinning message")

def poller(context):
    today = datetime.now().strftime("%d.%m")
    question = f"Футбол. {today}"

    print("PollBot will create a new poll")
    try:
        message = pollBot.sendPoll(chat_id=chat_id, question=question, options=["+", "-"], is_anonymous=False)
    except Exception as error:
        print(error)
    print(f"PollBot created a new poll with question \"{question}\"")
    pinMessage(message)
    scheduleUnpinningMessage(message)

time = time(18,00,50, 0000)
jobQueue.run_daily(poller, time, days=(0,1,2,3,4,5,6))
jobQueue.start()
print("PollBot started")
updater.idle()
print("PollBot finished")
