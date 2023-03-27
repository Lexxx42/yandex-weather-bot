# weather-bot

* Simple weather bot python-telegram-bot v20.0b0

---

## Used libraries

* https://docs.python-telegram-bot.org/en/v20.0b0/
* Coded with Python 3.11.1

---

## How to start the bot?

1. Created new bot from https://t.me/BotFather if you don't have one
2. Get token for API Yandex Weather https://yandex.com/dev/weather/
3. Install all requirements from requirements.txt

``` shell
pip install -r requirements.txt  
```

4. Create file .env in project root
5. Copy the line into you .env file with token provided by BotFather

``` shell
BOT_TOKEN=YOUR_BOT_TOKEN  
```

6. Copy the line into you .env file with token provided by Yandex.Weather API

``` shell
TOKEN_YANDEX_WEATHER=YOUR_API_YANDEX_WEATHER_TOKEN  
```

# New features with docker

## If there is an error about lack of access, add the current user to the docker group:

```shell
sudo usermod -a -G docker [user]
newgrp docker
```

## Use this sequence of commands to run the container:

1. To run the application in docker, you need to install docker-compose:

```shell
sudo apt install docker-compose 
```

2. Clone the repository

```shell
git clone https://github.com/Lexxx42/yandex-weather-bot.git
```

3. Change directory to project dir

```shell
cd yandex-weather-bot/
```

4. Add your tokens for telegram bot and yandex weather

```shell
nano .env
```

```
BOT_TOKEN=YOUR_BOT_TOKEN
TOKEN_YANDEX_WEATHER=YOUR_API_YANDEX_WEATHER_TOKEN
```


Don't forget to save changes!

5. Start the build

```shell
docker-compose up --build
```
