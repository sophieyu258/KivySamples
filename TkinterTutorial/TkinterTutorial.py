from tkinter import *
from tkinter.filedialog import askopenfilename

def NewFile():
    print("New File!")
def OpenFile():
    name = askopenfilename()
    print( name )
def About():
    print("This is a simple example of a menu")
    
def hello(event):
    print("Single Click, Button-l") 
def double_click(event):                           
    print("Double Click") 

def motion(event):
    print("Mouse position: (%s %s)" % (event.x, event.y))
    return

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

colours = ['red','green','orange','white','yellow','blue']

r = 0
for c in colours:
    widget = Label(text=c, relief=RIDGE,width=15)
    widget.grid(row=r,column=0)
    widget.bind('<Button-1>', hello)
    widget.bind('<Double-1>', double_click)
    ent = Entry(bg=c, relief=SUNKEN,width=10)
    ent.grid(row=r,column=1)
    ent.bind('<Motion>',motion)
    r = r + 1

mainloop()