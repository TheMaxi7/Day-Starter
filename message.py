# Importing necessary modules
import asyncio
import os
import time
from datetime import date

import requests
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

today = date.today()
day_month_format = str(today.strftime("%d/%m"))
user_name = "your name here"

# Function to send the message to the user
async def send_message():
    content = f"😊 Good Morning {user_name}!! 😊\nHere there is your morning wrap up:\n \n"

    birthdays = birthday.get_name(day_month_format)

    if len(birthdays) == 1:
        content += f"Firstly, don't forget today is {birthdays[0]}'s birthday!! 🎉🎉\n \n"
    elif len(birthdays) > 1:
        names = "'s, ".join(birthdays)
        content += f"Firstly, don't forget today is {names}'s birthdays!!🎉🎉\n \n"

    content += call.get_weather() + call.get_news() + call.get_markets_data()

    await bot.send_message(chat_id=CHAT_ID, text=content, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


# Schedule the job to run every day at 6 am
async def scheduled_job():
    schedule.every().day.at("06:00").do(asyncio.create_task, send_message())
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

async def main():
    await scheduled_job()

asyncio.run(main())
