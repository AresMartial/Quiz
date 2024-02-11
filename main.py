from data_fetcher import DataFetcher
from quiz_brain import QuizBrain
from question_model import Question

if __name__ == '__main__':

    data_fetcher = DataFetcher()
    quiz = QuizBrain()

    category, difficulty, amount, type_of_questions = quiz.manage_settings(data_fetcher)

    question_data = data_fetcher.get_trivia_questions(category, difficulty, amount, type_of_questions)

    question_bank = [Question(question["question"], question["correct_answer"], question["incorrect_answers"]) for
                     question in question_data]

    quiz.make_user_answer(question_bank)
