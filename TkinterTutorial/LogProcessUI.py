from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

inputFilePath = ""


def OpenFile():
    global inputFilePath
    inputFilePath = askopenfilename()
    print( inputFilePath )
    inputFile.set(inputFilePath)

def ProcessFile():
    print(inputFilePath)

def About():
    messagebox.showinfo("About this program", "Data processing tool for WorkTimeTracker by Bin Hang")


root = Tk()
root.geometry("320x240+30+30") 

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_command(label="Process", command=ProcessFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

Label(text="Please choose the input file:").pack()
inputFile = StringVar(root)
fileEntry = Entry(root, relief=SUNKEN, textvariable=inputFile).pack(fill="x", expand=True)

mainloop()
