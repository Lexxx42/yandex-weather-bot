import requests as req
import json
import logging
from ... import tokens
from os import path

FILE_NAME_JSON = 'yandex_weather.json'
headers = {'X-Yandex-API-Key': tokens.token_yandex_weather}


def yandex_weather(latitude, longitude):
    url_yandex = f'https://api.weather.yandex.ru/v2/forecast?lat={latitude}&lon={longitude}&[lang=ru_RU]'
    yandex_req = req.get(url_yandex, headers=headers)
    logging.info(f"made request to API yandex {url_yandex}")
    return yandex_req


def save_to_file(data):
    with open(FILE_NAME_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
        logging.info(f"data saved to {FILE_NAME_JSON}")


def get_weather_yandex(lat: float, lon: float):
    latitude_input = lat
    longitude_input = lon
    data_request = yandex_weather(latitude_input, longitude_input).json()
    logging.info("data collected from response")
    save_to_file(data_request)
    logging.info("started collecting weather data from yandex")
    yandex_json = load_from_file()
    weather = dict()
    # URL.
    weather['url'] = yandex_json['info']['url']
    # Location.
    weather['location'] = dict()
    weather['location']['country'] = yandex_json['geo_object']['country']['name']
    weather['location']['region'] = yandex_json['geo_object']['province']['name']
    if yandex_json['geo_object']['locality']:
        weather['location']['city'] = yandex_json['geo_object']['locality']['name']
    else:
        weather['location']['city'] = "Unlocated"
    if yandex_json['geo_object']['district']:
        weather['location']['district'] = yandex_json['geo_object']['district']['name']
    else:
        weather['location']['district'] = "Unlocated"
    # Current weather.
    weather['fact'] = dict()
    weather['fact']['temp'] = yandex_json['fact']['temp']
    weather['fact']['feels_like'] = yandex_json['fact']['feels_like']
    weather['fact']['condition'] = yandex_json['fact']['condition']
    weather['fact']['pressure_mm'] = yandex_json['fact']['pressure_mm']
    weather['fact']['humidity'] = yandex_json['fact']['humidity']
    weather['fact']['wind_speed'] = yandex_json['fact']['wind_speed']
    # Adding keys.
    keys = ['evening', 'morning', 'night', 'day']
    # Forecasts.
    for key in keys:
        weather[key] = dict()
        for i, item in enumerate(yandex_json['forecasts']):
            if not (weather.get(key)).get("temp"):
                weather[key]['temp'] = item['parts'][key]['temp_avg']
            if not (weather.get(key)).get("condition"):
                weather[key]['condition'] = item['parts'][key]['condition']
    logging.info(f"weather from yandex: {weather}")
    return weather


def load_from_file():
    if path.exists(FILE_NAME_JSON):
        with open(FILE_NAME_JSON, encoding="utf-8") as file:
            data = json.load(file)
        logging.info(f"json {FILE_NAME_JSON} loaded")
    else:
        data = None
        logging.info(f"there is no file {FILE_NAME_JSON}")
    return data
