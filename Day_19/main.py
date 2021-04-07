from turtle import Turtle, Screen

dora = Turtle()
screen = Screen()


def move_forward():
    dora.forward(15)


def move_back():
    dora.back(15)


def move_up():
    dora.left(15)


def move_down():
    dora.right(15)


def clear():
    screen.reset()


screen.listen()
screen.onkeypress(fun=move_forward, key="Up")
screen.onkeypress(fun=move_back, key="Down")
screen.onkeypress(fun=move_up, key="Left")
screen.onkeypress(fun=move_down, key="Right")
screen.onkeypress(fun=clear, key="c")
screen.exitonclick()
