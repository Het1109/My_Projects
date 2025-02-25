from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)

def right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward,"w" )
screen.onkey(move_backward,"s" )
screen.onkey(right,"d" )
screen.onkey(left,"a" )
screen.onkey(clear,"c" )



screen.exitonclick()
