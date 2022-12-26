import logging
import json
from os import path

FILE_NAME_JSON = 'yandex_weather.json'


def get_weather_yandex():
    logging.info("data collected from response")
    conditions = {'clear': 'ясно', 'partly-cloudy': 'малооблачно', 'cloudy': 'облачно с прояснениями',
                  'overcast': 'пасмурно', 'drizzle': 'морось', 'light-rain': 'небольшой дождь',
                  'rain': 'дождь', 'moderate-rain': 'умеренно сильный', 'heavy-rain': 'сильный дождь',
                  'continuous-heavy-rain': 'длительный сильный дождь', 'showers': 'ливень',
                  'wet-snow': 'дождь со снегом', 'light-snow': 'небольшой снег', 'snow': 'снег',
                  'snow-showers': 'снегопад', 'hail': 'град', 'thunderstorm': 'гроза',
                  'thunderstorm-with-rain': 'дождь с грозой', 'thunderstorm-with-hail': 'гроза с градом'
                  }
    wind_dir = {'nw': 'северо-западное', 'n': 'северное', 'ne': 'северо-восточное', 'e': 'восточное',
                'se': 'юго-восточное', 's': 'южное', 'sw': 'юго-западное', 'w': 'западное', 'с': 'штиль'}

    yandex_json = load_from_file()
    yandex_json['fact']['condition'] = conditions[yandex_json['fact']['condition']]
    print(yandex_json)
    print(conditions)
    print("***")
    yandex_json['fact']['wind_dir'] = wind_dir[yandex_json['fact']['wind_dir']]
    for i, item in enumerate(yandex_json['forecasts']):
        print(item['parts'])
    exit()
    for j, parts in enumerate(yandex_json['forecasts']['parts']):
        parts['condition'][j] = conditions[parts['condition']]
        parts['wind_dir'][j] = wind_dir[parts['wind_dir']]

    pogoda = dict()
    params = ['condition', 'wind_dir', 'pressure_mm', 'humidity']
    for parts in (yandex_json['forecasts'])['parts']:
        pogoda[parts['part_name']] = dict()
        pogoda[parts['part_name']]['temp'] = parts['temp_avg']
        for param in params:
            pogoda[parts['part_name']][param] = parts[param]

    pogoda['fact'] = dict()
    pogoda['fact']['temp'] = yandex_json['fact']['temp']
    for param in params:
        pogoda['fact'][param] = yandex_json['fact'][param]

    pogoda['link'] = yandex_json['info']['url']
    print(pogoda)
    return pogoda


def load_from_file():
    if path.exists(FILE_NAME_JSON):
        with open(FILE_NAME_JSON, encoding="utf-8") as file:
            data = json.load(file)
        print(f"json {FILE_NAME_JSON} loaded")
    else:
        data = None
        print(f"there is no file {FILE_NAME_JSON}")
    return data


get_weather_yandex()
