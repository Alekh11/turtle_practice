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

walker = Turtle()
walker.width(9)
walker.speed(0)

direction = [0, 90, 180, 270]

for _ in range(200):
    walker.forward(40)
    walker.color(random_color())
    walker.setheading(random.choice(direction))



screen.exitonclick()