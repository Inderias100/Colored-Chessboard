from turtle import *
shelly = Turtle()

shelly.speed(0)

def grid(l, col):
    shelly.color(col)
    shelly.begin_fill()
    for x in range(4):
        shelly.forward(l)
        shelly.left(90)
    shelly.end_fill()

def thisrow(col):
    shelly.color(col)
    shelly.begin_fill()
    for y in range(4):
        for x in range(4):
            shelly.forward(20)
            shelly.left(90)
        if y == 3:
            break
        shelly.forward(40)
    shelly.end_fill()

def adjust(num=0):
    shelly.penup()
    shelly.left(90)
    shelly.forward(20)
    shelly.right(90)
    if num == 1:
        shelly.backward(100)
    elif num == 0:
        shelly.backward(140)
    shelly.pendown()

c1 = input("Enter First Color: ")
c2 = input("Enter Second Color: ")

grid(160, c1)
for z in range(4):
    thisrow(c2)
    adjust(1)
    thisrow(c2)
    adjust()









