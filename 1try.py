from math import*
from turtle import*
import turtle

x = int(input('how many numbers?'))
z = int(input('what times table?'))
y = []
speed(0)
penup()
goto(-200,0)
pendown()
rt(90)
a = turtle.pos()
y.append(a)
##def circle_coord():
for i in range(x):
    circle(200,-360/x)
    a = turtle.pos()
    y.append(a)

def shift_right(y):
    try:
        return y[1:] + [y[0]]
    except IndexError:
        return y

a = shift_right(y)

for i in a:
    y.append(i)

##goto(y[1])
d = 0          
for i in range(x):
    w = z * i
    penup()
    goto(y[d])
    d += 1
    pendown()
    goto(y[w])
        
exitonclick()



