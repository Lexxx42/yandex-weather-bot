import requests as req
import json
import logging
from ... import tokens

FILE_NAME_JSON = 'yandex_weather.json'
headers = {'X-Yandex-API-Key': tokens.token_yandex_weather}


# token = ""

def yandex_weather(latitude, longitude, token_yandex: str):
    url_yandex = f'https://api.weather.yandex.ru/v2/forecast?lat={latitude}&lon={longitude}&[lang=ru_RU]'
    yandex_req = req.get(url_yandex, headers={'X-Yandex-API-Key': tokens.token_yandex_weather})
    logging.info(f"made request to API yandex {url_yandex}")
    return yandex_req


async def save_to_file(data):
    with open(FILE_NAME_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
        logging.info(f"data saved to {FILE_NAME_JSON}")


async def get_weather_yandex(lat: float, lon: float):
    latitude_input = lat
    longitude_input = lon
    data_request = yandex_weather(latitude_input, longitude_input, tokens.token_yandex_weather).json()
    logging.info(f"data saved to {FILE_NAME_JSON}")
    await save_to_file(data_request)
