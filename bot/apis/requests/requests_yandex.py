import requests as req
import json
from .. import token_yandex_weather

latitude = 56.005363
longitude = 40.335331
FILE_NAME_JSON = 'yandex_weather.json'

headers = {'X-Yandex-API-Key': token_yandex_weather}


def yandex_weather(latitude, longitude, token_yandex: str):
    url_yandex = f'https://api.weather.yandex.ru/v2/forecast?lat={latitude}&lon={longitude}&[lang=ru_RU]'
    yandex_req = req.get(url_yandex, headers={'X-Yandex-API-Key': token_yandex_weather})
    return yandex_req


def save_to_file(data):
    with open(FILE_NAME_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
        print(f"save complete to {FILE_NAME_JSON}")


save_to_file(yandex_weather(latitude, longitude, token_yandex_weather).json())
