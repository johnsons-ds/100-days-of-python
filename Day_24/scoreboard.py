from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 32, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.high_score = self.new_high_score()
        self.sety(265)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_score()

    def new_high_score(self):
        with open("data.txt") as file:
            contents = int(file.read())
            return contents

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()
