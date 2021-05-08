from turtle import Turtle, Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player
import time

turtle = Player()
screen = Screen()
car = CarManager()
score = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Johnsons' Turtle Crossing Game!")

# TODO: A turtle moves forward when you press the 'Up' key. It can only move forwards, not back, left or right.

screen.listen()
screen.onkeypress(turtle.move_up, "Up")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    # TODO: Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left
    #  edge.
    car.create_car()
    car.move_cars()

    # TODO: When the turtle hits the top edge of the screen, it moves back to the original position and the player
    #  levels up. On the next level, the car speed increases.

    if turtle.finish_line():
        # reset the turtle position
        turtle.start()
        # speed the cars up
        car.new_level()
        # add a level
        score.add_score()

    # TODO: When the turtle collides with a car, it's game over and everything stops.
    for i in car.all_cars[0:]:
        if turtle.distance(i) < 20:
            game_on = False
            score.game_over()

screen.exitonclick()
