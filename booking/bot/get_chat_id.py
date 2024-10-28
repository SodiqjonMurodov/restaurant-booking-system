import requests
from core.settings import TELEGRAM_TOKEN


def get_chat_id():
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates'
    response = requests.get(url)
    data = response.json()
    print(data)  # Bu yerda chat_id ni izlang

get_chat_id()