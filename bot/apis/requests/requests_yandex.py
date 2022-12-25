import requests

r = requests.get('https://geocode-maps.yandex.ru/1.x', auth=('user', 'pass'))
print(r.text)
