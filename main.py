import turtle
from turtle import Turtle, Screen
import random
from extract import color_list

turtle.colormode(255)

tom = Turtle()
tom.speed("fastest")
tom.hideturtle()


def paint_dots():
    tom.pendown()
    tom.pensize(20)
    tom.dot(20, random.choice(color_list))
    tom.penup()
    tom.forward(50)


def complete_painting():
    y = -300
    for _ in range(10):
        y += 50
        tom.penup()
        tom.setheading(90)
        tom.sety(y)
        tom.setx(-300)
        tom.forward(50)
        tom.setheading(0)
        tom.forward(50)

        for _ in range(10):
            paint_dots()


complete_painting()

screen = Screen()
screen.exitonclick()
