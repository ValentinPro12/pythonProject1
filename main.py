import test_categories_jokes
import receiving_data_user

testApi = test_categories_jokes.TestJoke()
categories = testApi.get_all_categories()
jokes = testApi.get_jokes_from_all_categories()
question = receiving_data_user.GetJokesByUser().question()
