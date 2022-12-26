import logging
import json
from os import path

FILE_NAME_JSON = 'yandex_weather.json'


def get_weather_yandex():
    logging.info("started collecting weather data from yandex")
    yandex_json = load_from_file()
    weather = dict()
    # Location.
    weather['location'] = dict()
    weather['location']['country'] = yandex_json['geo_object']['country']['name']
    weather['location']['region'] = yandex_json['geo_object']['province']['name']
    weather['location']['city'] = yandex_json['geo_object']['locality']['name']
    weather['location']['district'] = yandex_json['geo_object']['district']['name']
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
    print(f"weather from yandex: {weather}")
    return weather


def load_from_file():
    if path.exists(FILE_NAME_JSON):
        with open(FILE_NAME_JSON, encoding="utf-8") as file:
            data = json.load(file)
        print(f"json {FILE_NAME_JSON} loaded")
    else:
        data = None
        print(f"there is no file {FILE_NAME_JSON}")
    return data


yandex_weather = get_weather_yandex()

print(f"""
🌈 Your location is:
country: {yandex_weather['location']['country']}, region: {yandex_weather['location']['region']},
city: {yandex_weather['location']['city']}, district: {yandex_weather['location']['district']}

Weather now:
🌡 temperature: {yandex_weather['fact']['temp']} °C
🤔 feels like: {yandex_weather['fact']['feels_like']} °C
⚡️ condition: {yandex_weather['fact']['condition']}
💨 atmospheric pressure: {yandex_weather['fact']['pressure_mm']} mm Hg
🌬 wind speed: {yandex_weather['fact']['wind_speed']} m/sec
💧 humidity: {yandex_weather['fact']['humidity']} %
""")
