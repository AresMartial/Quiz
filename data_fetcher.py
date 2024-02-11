import requests
import json


class DataFetcher:
    def get_categories(self):
        categories_api_url = "https://opentdb.com/api_category.php"

        response = requests.get(categories_api_url)

        if response.status_code == 200:
            # Parse the JSON response
            categories = json.loads(response.text)
            return categories
        else:
            # If the request was not successful, print an error message
            print(f"Error fetching categories. Status code: {response.status_code}")
            return []

    def get_trivia_questions(self, category=9, difficulty='medium', amount=10, type='boolean'):
        if amount > 50:
            print("Sorry you can't get more than 50 questions")
            return

        # Set up the API endpoint
        questions_api_url = f"https://opentdb.com/api.php?amount={amount}"

        # Prepare the parameters for the API request
        params = {
            'amount': amount,
            'category': category,  # 9 is General Knowledge, you can change it
            'difficulty': difficulty,
            'type': type,
        }

        # Make the API request
        response = requests.get(questions_api_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            questions = json.loads(response.text)

            # Extract and return the list of questions
            return questions['results']
        else:
            # If the request was not successful, print an error message
            print(f"Error fetching questions. Status code: {response.status_code}")
            return []

# question_data = [{
#     "response_code": 0,
#     "results": [
#         {
#             "type": "boolean",
#             "difficulty": "easy",
#             "category": "Science: Computers",
#             "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
#             "correct_answer": "True",
#             "incorrect_answers": ["False"]
#         },
#
#
# fff = {"response_code": 0, "results": [{"type": "multiple", "difficulty": "hard", "category": "Geography",
#                                         "question": "What is the capital of Wisconsin, USA?",
#                                         "correct_answer": "Madison",
#                                         "incorrect_answers": ["Milwaukee", "Wisconsin Dells", "Green Bay"]},
#                                        {"type": "multiple", "difficulty": "medium",
#                                         "category": "Entertainment: Video Games",
#                                         "question": "Which of the following characters is NOT playable in &quot;Resident Evil 6&quot;?",
#                                         "correct_answer": "Jill Valentine",
#                                         "incorrect_answers": ["Chris Redfield", "Sherry Birkin", "Helena Harper"]},
#
# categories_on_website = {
#     "trivia_categories": [{"id": 9, "name": "General Knowledge"},
#                           {"id": 10, "name": "Entertainment: Books"},
#                           {"id": 11, "name": "Entertainment: Film"},
#                           {"id": 12, "name": "Entertainment: Music"},
#                           {"id": 13, "name": "Entertainment: Musicals & Theatres"},
#                           {"id": 14, "name": "Entertainment: Television"},
#                           {"id": 15, "name": "Entertainment: Video Games"},
#                           {"id": 16, "name": "Entertainment: Board Games"},
#                           {"id": 17, "name": "Science & Nature"},
#                           {"id": 18, "name": "Science: Computers"},
#                           {"id": 19, "name": "Science: Mathematics"},
#                           {"id": 20, "name": "Mythology"},
#                           {"id": 21, "name": "Sports"},
#                           {"id": 22, "name": "Geography"},
#                           {"id": 23, "name": "History"},
#                           {"id": 24, "name": "Politics"},
#                           {"id": 25, "name": "Art"},
#                           {"id": 26, "name": "Celebrities"},
#                           {"id": 27, "name": "Animals"},
#                           {"id": 28, "name": "Vehicles"},
#                           {"id": 29, "name": "Entertainment: Comics"},
#                           {"id": 30, "name": "Science: Gadgets"},
#                           {"id": 31, "name": "Entertainment: Japanese Anime & Manga"},
#                           {"id": 32, "name": "Entertainment: Cartoon & Animations"}]}
