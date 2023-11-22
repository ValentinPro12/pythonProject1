import csv
import requests
from requests import Response


class Test_new_location:
    """класс для создание локаций """

    def __init__(self):
        self.base_url = 'https://rahulshettyacademy.com'
        self.post_resource = '/maps/api/place/add/json'
        self.get_resource = '/maps/api/place/get/json'
        self.key = '?key=qaclick123'

    def test_create_locations(self) -> None:
        """ Отправка 5 запросов на создание локаций и запись place_id в файл для дальнейшего чтения """
        place_id_file = open('place_id.txt', 'w+')
        for i in range(5):
            post_url = self.base_url + self.post_resource + self.key
            obj_json = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"

            }
            result = requests.post(post_url, json=obj_json)
            print(result.text)
            body = result.json().get('place_id')
            place_id_file.writelines(body + '\n')
        place_id_file.close()

    def get_location(self) -> None:
        """Чтение файла и отправка GET  запроса, по place_id"""
        with open('place_id.txt', 'r') as f:
            reader = csv.reader(f, delimiter='\n')

            for row in reader:
                place_id = row[0]
                url = self.base_url + self.get_resource + self.key + '&place_id=' + str(place_id)
                response = requests.get(url)
                print(response.status_code)
                self.check_status_code(response)
                self.print_response_by_get_info(response)
            f.close()

    @staticmethod
    def check_status_code(response: Response) -> None:
        """Проверка кода ответа сервера.
        :param response: ответ от сервера
        """
        status_codes = {
            200: "Запрос успешный. Статус код 200.",
            404: "Неуспешный запрос. Статус код 404.",
        }
        if response.status_code in status_codes:
            print(status_codes[response.status_code])

    @staticmethod
    def print_response_by_get_info(response: Response) -> None:
        """Печать информации об ответе в консоль по запросу get.

        :param response: ответ от сервера
        """
        response.encoding = "utf-8"
        body = response.json()
        print(
            f"location:{body.get('location')} \n"
            f"accuracy: {body.get('accuracy')} \n"
            f"name:{body.get('name')}\n"
            f"phone_number:{body.get('phone_number')}\n"
            f"id :{body.get('types')}\n"
            f"types :{body.get('types')}\n"
            f"website :{body.get('website')}\n"
            f"language :{body.get('language')}\n"
        )
