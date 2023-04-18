[![status: active](https://github.com/GIScience/badges/raw/master/status/active.svg)](https://github.com/GIScience/badges#active)

![image](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

# Day-Starter

This is a Python-based Telegram bot that sends a morning wrap-up message to the user, including daily weather, news, and market data, as well as any birthdays that are happening on that day. The bot uses the Telegram API, as well as external APIs for weather, news, and market data. The bot is scheduled to run every day at 6 am using the schedule library.

## Features

Sends a morning wrap-up message to the user on a daily basis, the message includes:
- Includes daily weather, news, and market data.
- Notifies the user of any birthdays happening on that day.

## Prerequisites

- Python 3.7 or higher
- Telegram API token
- OpenWeatherMap API key
- NewsAPI API key
- Alpha Vantage API key
- Google Sheets API credentials

## Installation

1. Clone the repository to your local machine.

```bash
git clone https://github.com/your_username/Day-Starter.git
```

2. Install the required packages.

```bash
pip install -r requirements.txt
```

3. Set up environment variables in a .env file in the project directory.

```bash
BOT_TOKEN=your_telegram_api_token
CHAT_ID=your_telegram_chat_id
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
NEWSAPI_API_KEY=your_newsapi_api_key
ALPHAVANTAGE_API_KEY=your_alphavantage_api_key
GOOGLE_APPLICATION_CREDENTIALS=path_to_google_sheets_api_credentials.json
```

4. Start the bot by running the `message.py` script.

```bash
python message.py
```

## Usage

The bot will automatically send a message to the specified Telegram chat at 6 am every day.
  
## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Altaro97/Day-Starter/blob/main/LICENSE) file for details.

## Acknowledgments

- The weather data is provided by the [OpenWeatherMap API](https://open-meteo.com/);
- The news data is provided by the [NewsAPI](https://newsapi.org/);
- The market data is provided by the [TwelveData API](https://twelvedata.com/) and [Clark J](https://rapidapi.com/user/rpi4gx);
- The birthday data is stored and retrieved from a Google Sheet using the [Google Sheets API](https://developers.google.com/sheets/api/guides/concepts).
