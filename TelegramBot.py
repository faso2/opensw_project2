import telegram
import schedule
import time
from datetime import datetime
import pytz
import asyncio

token = "6879534572:AAF8OWh2TNFfW3CyxvLVvfigaknSY5HXtJ8"
bot = telegram.Bot(token=token)
chat_id = "@gometsbot"

async def send_message():
    now = time.localtime()
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
    text = f'현재 시간 : {now_time}'
    print('sends massage')
    await bot.sendMessage(chat_id=chat_id, text=text)

def job():
    if 6 <= datetime.now(pytz.timezone('Asia/Seoul')).hour < 23:
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        new_loop.run_until_complete(send_message())

schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)