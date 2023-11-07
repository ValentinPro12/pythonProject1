import json
import sys

import requests


class TestJoke:
    url = 'https://api.chucknorris.io/jokes/random'
    categories_url = 'https://api.chucknorris.io/jokes/categories'

    def test_random_joke(self):
        """проверка  метода по возврату рандомных шуток """
        result = requests.get(self.url)
        self.check_status_and_response(result)

    def test_category_joke(self):
        """ проверка  метода по возврату шуток по категориям """
        categories = self.get_categories()
        if categories:
            for category in categories:
                category_url = self.url + '?category=' + category
                result = requests.get(category_url)
                self.check_status_and_response(result)
        print(f'катекория пустая')

    def get_categories(self):
        """получаем категории и убираем лишние символы """
        categories = self.categories_url
        result = requests.get(categories)
        arr = json.loads(result.text)
        return arr

    @staticmethod
    def check_status_and_response(result):
        """проверка статуса и получение ответа для печати в консоле"""
        TestJoke.not_found(result)
        if result.status_code == 200:
            print('Запрос успешный')
        else:
            print('Запрос вернулся с ошибкой')
        result.encoding = 'utf-8'
        body = result.json()
        print(f"Категория:{body.get('categories')} \n"
              f"дата создания: {body.get('created_at')} \n"
              f"icon_ur:{body.get('icon_url')}\n"
              f"id:{body.get('id')}\n"
              f"дата обновления :{body.get('updated_at')}\n"
              f"url:{body.get('url')}\n"
              f"значение:{body.get('value')}\n"
              )

    @staticmethod
    def not_found(result):
        """проверка на статус код 404"""
        non = requests.get(result.url[:-1])
        print(f'статус код:{result.status_code}')
        if non.status_code == 404:
            print(f'негативный тест с ошибкой в url {result.url[:-1]}')


testApi = TestJoke()
testApi.test_random_joke()
testApi.test_category_joke()
