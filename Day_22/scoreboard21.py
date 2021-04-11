from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(60, 250)
        self.write(arg=f"{self.r_score}", align=ALIGNMENT, font=FONT)
        self.goto(-60, 250)
        self.write(arg=f"{self.l_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
