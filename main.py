import test_categories_jokes
import receiving_data_user
import place
import requests

# testApi = test_categories_jokes.TestJoke()
# categories = testApi.get_all_categories()
# jokes = testApi.get_jokes_from_all_categories()
# question = receiving_data_user.GetJokesByUser().question()
testLocation = place.Test_new_location()
# testLocation.test_create_locations()
# testLocation.get_location()
testLocation.get_delete_location()

# url = "http://your_url_here"
#
# payload = {}
#
# headers = {
#     'Content-Type': 'application/json',
# }
#
# response = requests.delete(url, data=payload, headers=headers)
#
# print(response.text)

# with open('place_id.txt', 'r') as file:
#     place_ids = file.read().split()
#
# existing_place_ids = [place_id for place_id in place_ids if place_id != ' ']
# non_existing_place_ids = place_ids[1::2]
#
# print("Existing place_ids:", existing_place_ids)
# print("Existing place_ids:", non_existing_place_ids)
#
# for line_num, line in enumerate(file_content):
#     if line_num == 1 or line_num == 3:
#         delete_url = self.base_url + self.delete_resource + self.key
#         url = self.base_url + self.get_resource + self.key + '&place_id=' + line
#         obj_json = {
#             "place_id": line
#         }
#
#         response = requests.delete(delete_url, json=obj_json)
#         print(response.text)
#         response = requests.get(url)
#         self.check_status_code(response)
#         self.print_response_by_get_info(response)
