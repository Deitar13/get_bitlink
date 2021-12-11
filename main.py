import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()

BITLY_TOKEN = os.environ["API_BITLY_TOKEN"]
headers = {"Authorization": f"Bearer {BITLY_TOKEN}"}


def is_bitlink(input_url):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{input_url}'
    response = requests.get(url, headers=headers)
    return response.ok


def get_shorten_link(input_url):
    body = {"long_url": f"{input_url}"}
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()['id']


def get_count_clicks(input_url):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{input_url}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Данный скрипт принимает url адрес и
        создает из него короткую версию с помощью сервиса bitly.com.
        В случае если скрипту передать уже созданный битлинк,
        то скрипт отобразит количество переходов по этому битлинку"""
    )
    parser.add_argument('url', help='Введите url')
    args = parser.parse_args()
    parsed_url = urlparse(args.url)
    input_url = f"{parsed_url.netloc}{parsed_url.path}{parsed_url.query}"
    if is_bitlink(input_url):
        try:
            clicks_count = get_count_clicks(input_url)
            print("Количество кликов:", clicks_count)
        except requests.exceptions.HTTPError:
            print("количество кликов HTTPError")

    else:
        try:
            bitlink = get_shorten_link(args.url)
            print('Битлинк:', bitlink)
        except requests.exceptions.HTTPError:
            print("короткий url HTTPError")
