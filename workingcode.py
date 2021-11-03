from math import*
from turtle import*
import turtle

##basic settings and questions
x = int(input('how many numbers?'))
z = int(input('what times table?'))
y = []
speed(0)
penup()
goto(-300,0)
pendown()
rt(90)
a = turtle.pos()
y.append(a)
##def circle_coord():
for i in range(x):
    circle(300,-360/x)
    a = turtle.pos()
    y.append(a)

##shifting list to left
def shift_left(y):
    try:
        return y[1:] + [y[0]]
    except IndexError:
        return y

##shifting list so that list index is in range
e = y 
for i in range(z):
    e = shift_left(e)
    ##adding shifted list to base list
    for i in e:
        y.append(i)

##adding shifted list to base list
##for i in e:
    ##y.append(i)

print(len(y))
##drawing shape
d = 0          
for i in range(x):
    w = z * i
    penup()
    goto(y[d])
    d += 1
    pendown()
    goto(y[w])
        
exitonclick()



