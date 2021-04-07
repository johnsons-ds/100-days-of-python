# This code will not work in repl.it as there is no access to the colorgram package here.###
# We talk about this in the video tutorials##

# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     rgb_colors.append(tuple(color.rgb))
#
# print(rgb_colors)

from turtle import Turtle, Screen
import random

johnsons = Turtle()
screen = Screen()
screen.colormode(255)
johnsons.speed(6)
johnsons.penup()
johnsons.hideturtle()
screen.title("Welcome to Johnsons' Turtle!")

paint_colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
                (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
                (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
                (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153),
                (174, 94, 97), (176, 192, 209)]


johnsons.setheading(225)
johnsons.forward(300)
johnsons.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    johnsons.dot(20, random.choice(paint_colors))
    johnsons.forward(50)

    if dot_count % 10 == 0:
        johnsons.setheading(90)
        johnsons.forward(50)
        johnsons.setheading(180)
        johnsons.forward(500)
        johnsons.setheading(0)

screen.exitonclick()

# turtle.setworldcoordinates(llx, lly, urx, ury)
# Parameters
# llx – a number, x-coordinate of lower left corner of canvas
#
# lly – a number, y-coordinate of lower left corner of canvas
#
# urx – a number, x-coordinate of upper right corner of canvas
#
# ury – a number, y-coordinate of upper right corner of canvas
#
# Set up user-defined coordinate system and switch to mode “world” if necessary. This performs a screen.reset(). If
# mode “world” is already active, all drawings are redrawn according to the new coordinates.
