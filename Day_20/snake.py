from turtle import Turtle

# Blank list created for the starting blocks of the snake (3), using the below for loop. Creating constants (
# characterised by caps) helps to make it easier to tweak and change them in the future, and also, it helps to
# clearly identify which values are important in the code.

SNAKES_LIST = [(0, 0), (-20, 0), (-40, 0)]
snakes_body = []
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # 1. Create an initialising definition for the snake class. This should have three white square blocks developed
    # when the class is called.
    def __init__(self):
        self.segments = []
        self.make_body()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def make_body(self):
        for location in SNAKES_LIST:
            self.add_segment(location)

    def add_segment(self, location):
        new_segment = Turtle(shape="square")  # the 'new_segment' creates an instance of the object from the
        # turtle module.
        new_segment.penup()  # This runs the method penup from the turtle module, on the instance of the method.
        # The same applies to the color method as well.
        new_segment.color("white")
        new_segment.goto(location)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # 2. Create a method that moves the snake forward when the method is called on the snake object.

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
