import categories_jokes
import receiving_data_user
import place

testApi = categories_jokes.Joke()
categories = testApi.get_all_categories()
jokes = testApi.get_jokes_from_all_categories()
question = receiving_data_user.GetJokesByUser().question()
testLocation = place.Test_new_location()
testLocation.test_create_locations()
testLocation.get_location()
testLocation.get_delete_location()

