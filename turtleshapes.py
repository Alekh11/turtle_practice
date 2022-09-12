from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
colors = ["MediumSlateBlue","MediumSpringGreen","Violet","Gold","Lime","HotPink","Purple","Aquamarine","Red","LightSteelBlue","Lavender"]

# timmy_the_turtle.color("Black")


# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

timmy_the_turtle.speed(3)

def shapesdraw(sides):

    for shapemake in range (sides):
        degree = 360/sides
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(degree)
        
for shape_side_n in range (3,11):
    timmy_the_turtle.color(random.choice(colors))
    shapesdraw(shape_side_n)


























screen = Screen()
screen.exitonclick() 