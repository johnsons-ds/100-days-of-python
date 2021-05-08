from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_value = random.randint(-250, 250)
            new_car.goto(300, y_value)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)  # #The car is moving 'backward' as the 'setheading' is 0. This
            # means that it is facing east. Having it move forward would mean that the squares would be moving from
            # left to right of the screen.

    def new_level(self):
        self.car_speed += MOVE_INCREMENT
