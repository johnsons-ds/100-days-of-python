from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Johnsons' Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
food = Food()
score = Score()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect for collision with food.
    if snake.head.distance(food) < 17:
        # score.score += 1
        score.add_score()
        food.refresh()
        snake.extend()
        # print(score.score)

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        # game_on = False
        snake.reset_body()
        score.reset_score()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_on = False
            snake.reset_body()
            score.reset_score()


screen.exitonclick()
