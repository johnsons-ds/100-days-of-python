from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.sety(280)
        self.setx(-250)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.level += 1
        self.update_score()

    def game_over(self):  # This may need to be moved to the scoreboard file
        self.goto(0, 0)
        self.color('black')
        self.write("Game Over", move=False, align='center', font=("Courier", 40, "bold"))
