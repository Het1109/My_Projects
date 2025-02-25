from turtle import  Screen
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard


screen = Screen()
screen.tracer(0 )
screen.setup(600,600 )
screen.bgcolor("black")
screen.title("Het's Portable Snake Game")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right , "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

#   detect collision with food

    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()



# detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor()<-280 or snake.head.ycor() > 280 or snake.head.ycor()<-280 :
        # game_is_on = False
        # scoreboard.gameover()
        scoreboard.reset()
        snake.reset()

# detect collision with tail
# if head touch body --> game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            # game_is_on = False
            # scoreboard.gameover()
            scoreboard.reset()
            snake.reset()




















screen.exitonclick()

