from turtle import Screen
from scoreboard21 import Score
from paddles import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Johnsons' Pong Game")
screen.tracer(0)  # Tracer method controls the animation on the screen

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-380, 0))
screen.listen()
ball = Ball()
score = Score()

screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_on = True

while game_on:
    screen.update()  # When the animation is turned off, the screen needs to be updated in a while loop
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision
    if ball.ycor() > 285 or ball.ycor() < -285:
        # Needs to bounce
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # Detect if ball is out of bounds
    if ball.xcor() > 390:
        score.l_point()
        ball.reset_position()

    if ball.xcor() < -390:
        score.r_point()
        ball.reset_position()


screen.exitonclick()
