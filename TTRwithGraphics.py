import math
from tkinter.constants import TRUE
from graphics import *
from math import*

##loop
loop = 1
while loop == TRUE:
    ##basic settings and questions
    taille = int(input('what size window?'))
    num = int(input('how many numbers?'))
    TT = int(input('what times table?'))
    ##color choice
    color_1 = input('which color background?')
    color_2 = input('which color lines?')

    ##represent window and circle
    win = GraphWin('Times Tables Representation', taille, taille, autoflush=FALSE)
    win.setBackground(color_1)
    win.setCoords(-taille/2,-taille/2,taille/2,taille/2)
    radius = taille/2 - 50
    cercle = Circle(Point(0,0), radius)
    cercle.draw(win)
    ##draw lines
    for i in range(num):
        w = TT * i
        P1x = radius*(math.sin((pi/180)*(i*(360/num)+90)))
        P1y = radius*(math.cos((pi/180)*(i*(360/num)+90)))
        P2x = radius*(math.sin((pi/180)*(w*(360/num)+90)))
        P2y = radius*(math.cos((pi/180)*(w*(360/num)+90)))
        ligne = Line(Point(P1x,P1y),Point(P2x,P2y))
        ligne.setOutline(color_2)
        ligne.draw(win)
        
    win.getMouse()
    win.close()
    again = input('represent another time table?')
    if again == 'n':
        loop += 1



