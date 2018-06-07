
# https://www.python-course.eu/tkinter_canvas.php

from tkinter import *

canvas_width = 500
canvas_height = 150

oval_size = 3

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - oval_size ), ( event.y - oval_size )
   x2, y2 = ( event.x + oval_size ), ( event.y + oval_size )
   w.create_oval( x1, y1, x2, y2, fill = python_green )

master = Tk()
master.title( "Painting using Ovals" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )
    
mainloop()