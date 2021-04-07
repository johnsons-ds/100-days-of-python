from turtle import Turtle, Screen
import random


johnsons = Turtle()
screen = Screen()

johnsons.shape("turtle")
screen.title("Welcome to Johnsons' Turtle!")
screen.colormode(255)

# johnsons.color("blue")
# johnsons.pencolor(240,160,80)
johnsons.speed(0) #fast - 10, fastest - 0, normal - 6, slow - 3 and slowest - 1


# Drawing a dashed line
# for i in range(0,20):
#     johnsons.forward(5)
#     johnsons.penup()
#     johnsons.forward(5)
#     johnsons.pendown()

# #Drawing a triangle
# for i in range(0, 3):
#     johnsons.pencolor("red")
#     johnsons.forward(100)
#     johnsons.right(120)

# #Moving the turtle to make a square
# for i in range(0,4):
#     johnsons.pencolor("blue")
#     johnsons.forward(100)
#     johnsons.right(90)

# #Moving the turtle to make a pentagon
# for i in range(0,5):
#    johnsons.pencolor("green") 
#    johnsons.forward(100)
#    johnsons.right(72)

# #Moving the turtle to make an hexagon
# for i in range(0, 6):
#     johnsons.pencolor("orange")
#     johnsons.forward(100)
#     johnsons.right(60)

# #Drawing a heptagon
# for i in range(0, 7):
#     johnsons.pencolor("green")
#     johnsons.forward(100)
#     johnsons.right(51.5)

# #Moving the turtuel to make a oxagon
# for i in range(0, 8):
#     johnsons.pencolor("DarkOrchid")
#     johnsons.forward(100)
#     johnsons.right(45)

# #Drawing a nonagon
# for i in range(0, 9):
#     johnsons.pencolor("DarkGoldenrod1")
#     johnsons.forward(100)
#     johnsons.right(40)


# #Drawing a decagon
# for i in range(0, 10):
#     johnsons.pencolor("azure4")
#     johnsons.forward(100)
#     johnsons.right(36)

# color = ["azure4", "DarkGoldenrod1", "DarkOrchid", "green", "orange", "blue", "red"]

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         johnsons.forward(80)
#         johnsons.right(angle)

# for shape_side_n in range(3, 11):
#     johnsons.color(random.choice(color))
#     draw_shape(shape_side_n)


# Random walk drawing
# def move_forward():
#     range = [0, 90, 180, 270]
#     johnsons.forward(25)
#     johnsons.pensize(5)
#     johnsons.setheading(random.choice(range))


# for i in range(500):
#     johnsons.pencolor(random.choice(color))
#     move_forward()

# Changing the color randomly
    # screen.bgpic("Day_18/selfie.png")
def color_change():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# def move_forward():
#     range = [0, 90, 180, 270]
#     screen.colormode(255)
#     johnsons.pensize(5)
#     johnsons.forward(25)
#     johnsons.setheading(random.choice(range))

# for i in range(500):
#     johnsons.color(color_change())
#     move_forward()



# Drawing a spirograph
def draw_spirograph(size_gap):
    for i in range(int(360/size_gap)):
        johnsons.color(color_change())
        johnsons.setheading(johnsons.heading() + size_gap)
        johnsons.circle(100)

draw_spirograph(2)
screen.exitonclick()