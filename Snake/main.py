from turtle import Screen
import time

from Scoreboard import ScoreBoard
from food import Food
from snake import Snake


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game = True
while game:
    screen.update()
    time.sleep(0.15)
    snake.move()

    #Collision with food
    if snake.segments[0].distance(food) < 2:
        food.refresh()
        score.increase_score()
        snake.extend()

    #Collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        score.reset()
        snake.reset()

    #Collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 2:
            score.game_over()
            score.reset()
            snake.reset()



screen.exitonclick()