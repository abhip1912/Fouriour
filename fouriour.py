import turtle
from math import cos, sin

time = 0
radius = 100
Animation_speed = 1000
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor('black')
screen.tracer(0)

pen1 = turtle.Turtle()
pen1.pensize(1)
pen1.color('white')
pen1.speed(0)
pen1.hideturtle()

pen2 = turtle.Turtle()
pen2.pensize(20)
pen2.color('white')
pen2.speed(0)
pen2.hideturtle()

pen3 = turtle.Turtle()
pen3.pensize(1)
pen3.color('white')
pen3.speed(0)
pen3.hideturtle()

pen4 = turtle.Turtle()
pen4.pensize(1)
pen4.color('white')
pen4.speed(0)
pen4.hideturtle()

pen1.up()
pen1.sety(-radius)
pen1.down()
pen1.circle(radius)

count = 0
while True:
    pen3.goto(0, 0)
    pen3.dot(15)
    pen2.clear()
    pen2.dot(15, 'white')
    screen.update()
    x = radius * cos(time)
    y = radius * sin(time)
    pen4.up()
    pen4.goto(count, y)
    pen4.down()
    pen4.dot(5, 'white')
    pen3.goto(x, y)
    pen2.goto(x, y)
    time -= 0.0001*Animation_speed    # -= clockwise  && += Anticlockwise
    pen3.clear()
    count += 1
screen.exitonclick()
