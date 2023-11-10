from typing import List

import requests
from requests import Response


class TestJoke:

    def __init__(self):
        """Инициализация объекта."""
        self.base_url = 'https://api.chucknorris.io/jokes'

    def get_jokes_from_all_categories(self) -> List[str]:
        """Получить по одной шутке из каждой категории.

        :return: список с шутками
        """
        categories = self.get_all_categories()
        jokes = []
        for category in categories:
            category_url = self.base_url + '/random/?category=' + category
            response = requests.get(category_url)
            self.check_status_code(response)
            self.print_response_info(response)
            joke = response.json().get("value")
            jokes.append(joke)
        return jokes

    def get_all_categories(self) -> List[str]:
        """Получение всех категорий.

        :return: список категорий.
        """
        response = requests.get(self.base_url + "/categories")
        categories = response.json()
        return categories

    @staticmethod
    def check_status_code(response: Response):
        """Проверка кода ответа сервера.

        :param response: ответ от сервера
        """
        assert response.status_code == 200, f"Неуспешный запрос. Статус код {response.status_code}"
        print("Запрос успешный. Статус код 200.")

    @staticmethod
    def print_response_info(response: Response):
        """Печать информации об ответе в консоль.

        :param response: ответ от сервера
        """
        response.encoding = "utf-8"
        body = response.json()
        print(
            f"Категория:{body.get('categories')} \n"
            f"Дата создания: {body.get('created_at')} \n"
            f"icon_ur:{body.get('icon_url')}\n"
            f"id:{body.get('id')}\n"
            f"Дата обновления :{body.get('updated_at')}\n"
            f"url:{body.get('url')}\n"
            f"Значение:{body.get('value')}\n"
        )


testApi = TestJoke()
categories = testApi.get_all_categories()
jokes = testApi.get_jokes_from_all_categories()