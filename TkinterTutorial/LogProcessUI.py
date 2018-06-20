from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import ProcessLog

inputFilePath = ""
outputDirPath = ""


def OpenFile():
    global inputFilePath
    inputFilePath = askopenfilename()
    print( inputFilePath )
    inputFile.set(inputFilePath)

def OpenDir():
    global outputDirPath
    outputDirPath = askdirectory()
    print( outputDirPath )
    outputDir.set(outputDirPath)

def ProcessFile():
    print(inputFilePath)
    print(outputDirPath)
    if not inputFilePath:
        messagebox.showerror("Error", "Input file not selected!")
        return
    if not outputDirPath:
        messagebox.showerror("Error", "Output folder not selected!")
        return
    ProcessLog.ProcessFile(inputFilePath, outputDirPath)
    messagebox.showinfo("Success!", "Data processed successfully! Please check the output folder for results.")

def About():
    messagebox.showinfo("About this program", "Data processing tool for WorkTimeTracker by Bin Hang")


root = Tk()
root.title("Worktime data tool")
root.geometry("400x100+30+30") 

Grid.columnconfigure(root, 1, weight=1)

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open Input File...", command=OpenFile)
filemenu.add_command(label="Choose Output Dir...", command=OpenDir)
filemenu.add_command(label="Process", command=ProcessFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

Label(root, text="Input file:").grid(row = 0, column = 0, sticky=W)
inputFile = StringVar(root)
Entry(root, relief=SUNKEN, textvariable=inputFile).grid(row = 0, column = 1, sticky=N+S+E+W)
Button(root, text="...", command=OpenFile).grid(row = 0, column = 2)
Label(text="Output Folder:").grid(row = 1, column = 0, sticky=W)
outputDir = StringVar(root)
Entry(root, relief=SUNKEN, textvariable=outputDir).grid(row = 1, column = 1, sticky=N+S+E+W)
Button(root, text="...", command=OpenDir).grid(row = 1, column = 2)
Button(root, text="Go", command=ProcessFile).grid(row = 2, column = 1, pady=(10, 5))

mainloop()
