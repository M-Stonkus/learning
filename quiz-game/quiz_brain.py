class QuizBrain():
    def __init__(self, list):
        self.number = 0
        self.list = list
        self.score = 0

    def next_question(self):
        ans = input(f"Q{self.number+1}: {self.list[self.number].text} (True/False)?: ")
        self.check_answer(ans)
        self.number += 1

    def still_has_questions(self):
        return self.number < len(self.list)

    def check_answer(self, ans):
        if ans.lower() == self.list[self.number].answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")

        print(f"The correct answer was: {self.list[self.number].answer}.")
        print(f"Your current score is: {self.score}/{self.number + 1}")
        print("\n")