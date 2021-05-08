from turtle import Turtle

FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.shape("turtle")
        self.color("red")
        self.setheading(90)
        self.start()

    def move_up(self):
        self.forward(10)

    def start(self):
        self.goto(0, -280)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

