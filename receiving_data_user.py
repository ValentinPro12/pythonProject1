from typing import List
import test_categories_jokes
import requests


class GetJokesByUser:
    def __init__(self):
        """Инициализация объекта."""
        self.base_url = 'https://api.chucknorris.io/jokes'

    def question(self) -> List[str]:
        """Получение всех категорий для отображения пользователю"""
        jokes = []
        categories = test_categories_jokes.TestJoke().get_all_categories()
        print(
            f"Выберите категорию:{categories}")
        """Запрашиваем категорию у пользователя"""
        category_by_user = input()

        """Проверка ввода категолии и получение шутки"""
        if category_by_user in categories:
            category_url = self.base_url + '/random/?category=' + category_by_user
            response = requests.get(category_url)
            test_categories_jokes.TestJoke().check_status_code(response)
            test_categories_jokes.TestJoke().print_response_info(response)
            joke = response.json().get("value")
            jokes.append(joke)
        else:
            print(f'Данной категории не существует')
        return jokes
