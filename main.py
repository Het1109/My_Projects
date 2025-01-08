from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time





screen = Screen()
screen.setup(800,600)
screen.title("Het's Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350 , 0))
l_paddle = Paddle((-350 , 0))
ball = Ball()
scoreborad = Scoreboard()






screen.listen()
screen.onkey(r_paddle.go_up , "Up")
screen.onkey(r_paddle.go_down , "Down")


screen.onkey(l_paddle.go_up , "w")
screen.onkey(l_paddle.go_down , "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#detect the collision with upper and lower wall to reflect back

    if ball.ycor() > 280 or ball.ycor() < -280:
#needs to bounce
        ball.bounce_y()



#detect collision with  paddle
    if (ball.distance(r_paddle) < 50 and  ball.xcor() > 320
            or
            ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()


# detect if right paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreborad.l_point()

# detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreborad.r_point()


screen.exitonclick()