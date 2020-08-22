import turtle
from math import cos, sin

time = 0
radius = 200
speed = 5

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor('black')
screen.tracer(0)

pen1 = turtle.Turtle()
pen1.pensize(5)
pen1.color('white')
pen1.speed(0)
pen1.hideturtle()

pen2 = turtle.Turtle()
pen2.pensize(20)
pen2.color('white')
pen2.speed(0)
pen2.hideturtle()

pen1.up()
pen1.sety(-radius)
pen1.down()
pen1.circle(radius)

while True:
    pen2.clear()
    pen2.dot(30, 'white')
    screen.update()
    x = radius * cos(time)
    y = radius * sin(time)
    pen2.goto(x, y)
    time += 0.0001*speed
screen.exitonclick()
