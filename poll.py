from datetime import datetime, time
from os import getenv
from pytz import timezone

from telegram.ext import Updater, Handler, MessageHandler, Filters
from telegram import Update, Poll

config = ""
# chat_id = getenv("CHAT_ID")
usmShopingId = 1001497859545

updater = Updater(token=config, use_context=True)

def poller(context):
    bot = context.bot
    today = datetime.now().strftime("%d.%m")
    question = f"Футбол. {today}"
    bot.sendPoll(chat_id=-1001497859545, question=question, options=["+", "-"], is_anonymous=False)

time = time(13,20,00, 0000)
updater.dispatcher.job_queue.run_daily(poller, time, days=(6,))

updater.start_polling()
updater.idle()



# https://api.telegram.org/bot688265239:AAEq33i2ipJ-1aZioAnodAvFr8Pm6tpSe9A/getUpdates // get chat id