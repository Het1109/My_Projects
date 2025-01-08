import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width= 500 , height= 400)
user_bet = screen.textinput(title="try Your Luck" , prompt="Which colour?")

is_race = False
colors = ["red" , "green" , "blue" , "black" , "orange" , "yellow"]
y_positions = [-70 , -40 ,  -10 , 20 , 50 , 80]
all_turtle = []

for turtleIndex in range(6):
    new_turtle = Turtle(shape="turtle" )
    new_turtle.color(colors[turtleIndex])
    new_turtle.penup()
    new_turtle.goto(x=-230 , y = y_positions[turtleIndex])
    all_turtle.append(new_turtle)

if user_bet:
    is_race = True


while is_race:



    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race = False
            win = turtle.pencolor()
            if win == user_bet:
                print(f"You have won! The {win} turtle is winner")
            else:
                print(f"You have lost! The {win} turtle is winner")

        rand_dist = random.randint(0 , 10)
        turtle.forward(rand_dist)

screen.exitonclick()