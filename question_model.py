class Question:
    def __init__(self, text: str, answer: str, wrong_answers: list, difficulty="easy"):
        self.text = text
        self.answer = answer
        self.wrong_answers = wrong_answers
        self.difficulty = difficulty
