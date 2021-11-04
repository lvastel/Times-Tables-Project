import math
from graphics import *
from math import*

##basic settings and questions
x = int(input('how many numbers?'))
z = int(input('what times table?'))
##represent window

win = GraphWin('Times Tables Representation', 800, 800)
win.setBackground('blue')
win.setCoords(-400,-400,400,400)
e = Circle(Point(0,0), 300)
e.draw(win)
for i in range(x):
    w = z * i
    a = 300*(math.sin((pi/180)*(i*(360/x)+90)))
    b = 300*(math.cos((pi/180)*(i*(360/x)+90)))
    c = 300*(math.sin((pi/180)*(w*(360/x)+90)))
    d = 300*(math.cos((pi/180)*(w*(360/x)+90)))
    l = Line(Point(a,b),Point(c,d))
    l.draw(win)
    


win.getMouse()
win.close()

