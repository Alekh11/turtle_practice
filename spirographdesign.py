
from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


screen = Screen()
screen.bgcolor("black")

designer = Turtle()
designer.speed(0)


def spirograph(spaces):
    for _ in range(int(360/spaces)):
        
        designer.color(random_color())
        designer.circle(100)
        designer.setheading(designer.heading() + spaces)


spirograph(5)

screen.exitonclick()