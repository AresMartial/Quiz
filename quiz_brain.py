import html
from question_model import Question
import random


class QuizBrain:
    def __init__(self):
        self.score = 0
        self.asked_questions = 0

    def make_user_answer(self, question_bank: list[Question]):
        for i in range(len(question_bank)):
            question = question_bank[i]
            possible_answers = question.wrong_answers + [question.answer]
            random.shuffle(possible_answers)

            print(f"Q.{self.asked_questions + 1}: {html.unescape(question.text)}")
            for element in range(len(possible_answers)):
                print(f"{element + 1}: {possible_answers[element]}")
            user_answer = int(input("Answer: ")) - 1
            if possible_answers[user_answer] == question.answer:
                print("You got it right!")
                self.score += 1
                self.asked_questions += 1
            else:
                print("That's wrong.")
                self.asked_questions += 1
            print(f"The correct answer was: {question.answer}.\n"
                  f"Your score is: {self.score}/{self.asked_questions}\n")

    def manage_settings(self, data_fetcher):
        user_needs_settings = input('Do you want to customise quiz - choose category, difficulty, etc? (y/n): ')
        if user_needs_settings == 'y':

            user_needs_type = input("Do you want to choose the type of questions? (y/n): ")
            if user_needs_type == 'y':
                type_of_questions = input('Choose between true/false ("tf") or multiple choice ("mc" questions: ')
                if type_of_questions == 'tf':
                    type_of_questions = 'boolean'
                elif type_of_questions == 'mc':
                    type_of_questions = 'multiple'
            else:
                type_of_questions = 'boolean'

            user_needs_category = input("Do you want to choose category? (y/n): ")
            if user_needs_category == 'y':
                available_categories = data_fetcher.get_categories()["trivia_categories"]
                for category in available_categories:
                    print(f"{category["id"] - 8} - {category["name"]}")
                category = int(input('Please enter preferable category id: ')) + 8
            else:
                category = 9

            user_needs_difficulty = input("Do you want to choose difficulty? (y/n): ")
            if user_needs_difficulty == 'y':
                difficulty_number = int(
                    input('Please choose preferable difficulty: \n1 - easy \n2 - medium \n3 - hard\n'))
                if difficulty_number == 1:
                    difficulty = 'easy'
                elif difficulty_number == 2:
                    difficulty = 'medium'
                elif difficulty_number == 3:
                    difficulty = 'hard'
                else:
                    print("Wrong input, setting difficulty to default - medium")
                    difficulty = 'medium'
            else:
                difficulty = 'medium'

            user_needs_amount = input("Do you want to choose amount of questions? (y/n): ")
            if user_needs_amount == 'y':
                amount = int(input('Please choose preferable amount of questions below 50: '))
            else:
                amount = 10
        else:
            category = 18
            difficulty = 'medium'
            amount = 5
            type_of_questions = 'boolean'

        return category, difficulty, amount, type_of_questions
