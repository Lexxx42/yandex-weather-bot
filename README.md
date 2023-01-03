# yandex-weather-bot

* Simple weather bot python-telegram-bot v20.0b0.
Uses Yandex.Weather API and provides weather forecast.
---

## Used libraries

* https://docs.python-telegram-bot.org/en/v20.0b0/
* Coded with Python 3.11.1

---

## How to start the bot?

1. Create a new bot from https://t.me/BotFather if you don't have one
2. Get the token for API Yandex Weather https://yandex.com/dev/weather/
3. Install all requirements from requirements.txt

``` shell
pip install -r requirements.txt  
```

4. Create file .env in project root
5. Copy the line into your .env file with token provided by BotFather
``` shell
BOT_TOKEN=YOUR_BOT_TOKEN  
```
6. Copy the line into your .env file with token provided by Yandex.Weather API
``` shell
TOKEN_YANDEX_WEATHER=YOUR_API_YANDEX_WEATHER_TOKEN  
```
## To Do

1. Get off writing data from API.
2. Optimaze data collection.
