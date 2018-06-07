from tkinter import *
from tkinter.filedialog import *
from tkinter.colorchooser import askcolor                  

def colorcallback():
    result = askcolor(color="#6A9662", 
                      title = "Bernd's Colour Chooser") 
    print(result)
    
root = Tk()

def filecallback():
    name= askopenfilename() 
    print(name)
    
def dircallback():
    name= askdirectory() 
    print(name)

Button(root, text='File Open', command=filecallback).pack(fill=X)

Button(root, text='Directory Open', command=dircallback).pack(fill=X)

Button(root, 
       text='Choose Color', 
       fg="darkgreen", 
       command=colorcallback).pack(fill=X)

Button(text='Quit', 
       command=root.quit,
       fg="red").pack(fill=X)

mainloop()