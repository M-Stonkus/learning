from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0

        with open("./hscore.txt") as file:
            self.highscore = int(file.read())

        self.penup()
        self.setpos((0, 265))
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.setpos((0, 0))
        self.write("GAME OVER", False, align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("./hscore.txt", "w") as file:
                file.write(str(self.highscore))

        self.score = 0
        self.update()




