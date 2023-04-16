import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Load API keys from environment variables
NEWS_API = os.getenv('NEWS_API')
TWELVEDATA_API = os.getenv('TWELVEDATA_API')
FAG_API = os.getenv('FAG_API')

class Calls:
    def get_weather(self):
        url = "https://api.open-meteo.com/v1/forecast?latitude=46.07&longitude=13.24&forecast_days=1&timezone=GMT&daily=temperature_2m_max&daily=temperature_2m_min&daily=precipitation_probability_mean&daily=windspeed_10m_max"
        message = "🌦 🌦 🌦 Weather news 🌦 🌦 🌦 \n \n"

        # Make API request and parse JSON response
        response = requests.get(url)
        data = response.json()

        # Extract relevant data from response
        date = data['daily']['time'][0]
        temp_max = data['daily']['temperature_2m_max'][0]
        temp_min = data['daily']['temperature_2m_min'][0]
        precip_prob = data['daily']['precipitation_probability_mean'][0]
        max_wind_speed = data['daily']['windspeed_10m_max'][0]

        # Format message with extracted data
        message += f"Date: {date}\nMax Temperature: {temp_max}°C Min Temperature: {temp_min}°C\nPrecipitation probability: {precip_prob}%\nMax wind speed: {max_wind_speed} km/h\n \n \n"
        return message

    def get_news(self):
        url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={NEWS_API}'
        message="🌏 🌏 🌏 Daily News 🌏 🌏 🌏 \n \n"

        # Make API request and parse JSON response
        response = requests.get(url)
        articles = response.json()['articles']

        # Extract relevant data from response and format message
        for article in articles:
            title = article['title']
            description = article['description']
            link = article['url']
            message += f"Title: {title}\nDescription: {description}\nLink: <a href='{link}'>Click here</a>\n\n\n"
        return message
    def get_markets_data(self):
        # API endpoints and queries
        url = "https://twelve-data1.p.rapidapi.com/quote"
        fear_and_greed_url = "https://fear-and-greed-index.p.rapidapi.com/v1/fgi"
        btc_price_query = {"symbol":"BTC/USD","interval":"1day"}
        eth_price_query = {"symbol": "ETH/USD","interval":"1day"}

        # API headers
        headers = {
            "X-RapidAPI-Key": f"{TWELVEDATA_API}",
            "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
        }
        fear_and_greed_headers = {
            "X-RapidAPI-Key": f"{FAG_API}",
            "X-RapidAPI-Host": "fear-and-greed-index.p.rapidapi.com"
        }

        # Request data from APIs
        btc = requests.request("GET", url, headers=headers, params=btc_price_query)
        eth = requests.request("GET", url, headers=headers, params=eth_price_query)
        response = requests.request("GET", fear_and_greed_url, headers=fear_and_greed_headers)

        # Parse data from API responses
        btc_data = btc.json()
        btc_price = btc_data['close']
        btc_change = btc_data['percent_change']
        eth_data = eth.json()
        eth_price = eth_data['close']
        eth_change = eth_data['percent_change']
        fear_and_greed_data = response.json()
        now_value = fear_and_greed_data['fgi']['now']['value']
        now_valueText = fear_and_greed_data['fgi']['now']['valueText']
        oneWeekAgoValue_value = fear_and_greed_data['fgi']['oneWeekAgo']['value']
        oneWeekAgoValue_valueText = fear_and_greed_data['fgi']['oneWeekAgo']['valueText']

        # Construct message with data
        message = "💲 💲 💲 Markets update 💲 💲 💲 \n \n"
        message += f"₿ BTC/USD: {btc_price}  24h Change: {btc_change}%\n"
        message += f"⬨ ETH/USD: {eth_price}  24h Change: {eth_change}%\n \n"
        message += "🐻 🐻 🐻 Fear and Greed Index 🦬 🦬 🦬\n \n"
        message += f"Today: {now_value} - {now_valueText}\n"
        message += f"One week ago: {oneWeekAgoValue_value} - {oneWeekAgoValue_valueText}\n"
        message += "Link: <a href='https://edition.cnn.com/markets/fear-and-greed'>Click here</a>"

        return message




