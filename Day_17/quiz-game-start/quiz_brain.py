#TODO: asking the questions
#TODO: checking if the answer was correct
#TODO: checking if we're the end of the quiz

# from main import question_bank
# from question_model import Question
# from data import question_data

class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list 
        self.score = 0

    def still_has_questions(self):
        #Using the comparison operators will produce a boolean value.
        #This would be the same as explicitly writing 'True' or 'False' as
        #a return value.
        return self.question_number < len(self.question_list)
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False?): ")
        #Checking the question number value
        # print(self.question_number)
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

