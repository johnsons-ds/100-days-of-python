from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

# User makes a bet on which turtle will win the race
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")

# While loop boolean value changes based on whether the user has provided an input at the start of the turtle game.

is_on = False
if user_bet:
    is_on = True

# Variables used to create turtles
y_positions = [-175, -87.5, 87.5, 175, 0]
color = ["red", "orange", "yellow", "green", "blue"]

# Blank list created for the 5 turtles to create using the below for loop.
all_turtles = []

for turtle_index in range(0, 5):
    turtles = Turtle(shape="turtle")
    turtles.penup()
    turtles.goto(-235, y_positions[turtle_index])
    turtles.color(color[turtle_index])
    all_turtles.append(turtles)


# While loop - this only runs if the user has put in an option when the game starts. This value is saved and compared to
# the turtle that reaches the x coordinates of 219/220. At this point, the game will stop and one of two statements will
# be printed in the console. I'm not yet sure how to make this appear as a window prompt.
while is_on:
    for instance in all_turtles:
        if instance.xcor() < 220:
            instance.forward(random.randint(0, 10))
        else:
            is_on = False
            winner = instance.pencolor()
            if winner == user_bet.strip().lower():
                print(f"Game Over! You guessed {user_bet}, and they won! The winner is the {winner} turtle.")
            else:
                print(f"Game Over! You guessed {user_bet} and they lost! The winner is the {winner} turtle.")

screen.exitonclick()
