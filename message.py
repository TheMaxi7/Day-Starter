# Importing necessary modules
import asyncio
import os
import pytz
from datetime import datetime, time, timedelta

import schedule
import telegram
from dotenv import load_dotenv
from telegram.constants import ParseMode

from data import Calls
from sheet import Birthdays

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Initialize telegram bot and other objects
bot = telegram.Bot(token=TOKEN)
birthday = Birthdays()
call = Calls()

user_name = "your name here"

# Function to send the message to the user
async def send_message():
    content = f"😊 Good Morning {user_name}!! 😊\nHere there is your morning wrap up:\n \n"

    today = datetime.now(pytz.timezone('Europe/Rome')).date()
    day_month_format = today.strftime("%d/%m")
    birthdays = birthday.get_name(day_month_format)

    if not birthdays:
        content = ""
    else:
        if len(birthdays) == 1:
            content += f"Firstly, don't forget today is {birthdays[0]}'s birthday!! 🎉🎉\n \n"
        elif len(birthdays) > 1:
            names = "'s, ".join(birthdays)
            content += f"Firstly, don't forget today is {names}'s birthdays!!🎉🎉\n \n"

    content += call.get_weather() + call.get_news() + call.get_markets_data()

    await bot.send_message(chat_id=CHAT_ID, text=content, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


# Schedule the job to run every day at 6 am
async def scheduled_job():
    while True:
        now = datetime.now(pytz.timezone('Europe/Rome'))
        scheduled_time = pytz.timezone('Europe/Rome').localize(
            datetime.combine(now.date(), time(hour=6, minute=0, second=0)))
        if now >= scheduled_time:
            scheduled_time += timedelta(days=1)
        time_to_wait = (scheduled_time - now).total_seconds()
        await asyncio.sleep(time_to_wait)
        await send_message()

async def main():
    while True:
        await scheduled_job()
        await asyncio.sleep(60)

asyncio.run(main())

