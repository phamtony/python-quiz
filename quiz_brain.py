class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def next_question(self):
        display_question = self.question_list[self.question_number].question
        answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {display_question}. (True/False)? ")
        self.check_answer(user_input, answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.user_score += 1
            print("Good Job!")
        else:
            print("You're wrong!")
        print(f"The correct answer was {answer}")
        print(f"Your current score is {self.user_score}/{self.question_number}")
        print("\n")
