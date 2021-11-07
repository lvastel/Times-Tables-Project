from tkinter import*
from math import*
import math

#Window
root = Tk()
root.title('Times Tables Representation-Interactive')
root.geometry("660x785")
root.configure(bg='#02277d')
root.resizable(False,False)

#Circle
can = Canvas(root,bg='#57a8ea' , width=650, height=650)
can.pack()
can.place(x=2.5, y=127)
can.configure(scrollregion=(-325,-325,325,325))
def TTR(yes):
    can.delete('all')
    size = Circle_size.get()
    circle = can.create_oval(-size,-size,size,size)
    num = Horizontal_1.get()
    TT = Horizontal_2.get()

    for i in range(num):
        w = TT * i
        P1x = -size*(math.sin((pi/180)*(i*(360/num)-90)))
        P1y = -size*(math.cos((pi/180)*(i*(360/num)-90)))
        P2x = size*(math.sin((pi/180)*(w*(360/num)-90)))
        P2y = size*(math.cos((pi/180)*(w*(360/num)-90)))
        line = can.create_line(P1x,P1y,P2x,P2y)
circle = can.create_oval(-320,-320,320,320)        

#sliders
Horizontal_1 = Scale(root,label='Number of points',bg='#48f9e2',bd=0 ,sliderlength=10,width=20,length=650, from_=10, to=1000, orient=HORIZONTAL,command=TTR)
Horizontal_1.pack()
Horizontal_1.place(x =2.5, y = 2.5)
Horizontal_2 = Scale(root,label='Times table number',bg='#48f9e2',bd=0,sliderlength=10,width=20,length=322, from_=2, to=300, orient=HORIZONTAL,command=TTR)
Horizontal_2.pack()  
Horizontal_2.place(x = 331, y = 65) 
Circle_size = Scale(root,label='Circle Size',bg='#48f9e2',bd=0 ,sliderlength=10,width=20,length=322, from_=320, to=100, orient=HORIZONTAL,command=TTR)
Circle_size.set(320)
Circle_size.pack()
Circle_size.place(x=2.5,y=65)
root.mainloop()