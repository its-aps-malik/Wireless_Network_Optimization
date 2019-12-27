# this generates the GUI for our simulation

from tkinter import *
import os

def changeLater():
    print("lol")

no_of_nodes = 0

def loadUI():

    root = Tk()


    root.title("Wireless Netework Simulator")
    root.geometry("800x600")
    root.resizable(0, 0)


    menubar = Menu(root)
    root.config(menu=menubar)

    filemenu = Menu(menubar)
    menubar.add_cascade(label="File" , menu=filemenu)
    filemenu.add_command(label="New run" , command=changeLater)
    filemenu.add_command(label="Exit" , command=changeLater)

    editmenu = Menu(menubar)
    menubar.add_cascade(label="Edit" , menu=editmenu)
    editmenu.add_command(label="Undo" , command=changeLater)
    editmenu.add_command(label="Redo" , command=changeLater)


    status_notification = Label(root , text="some crap..." , bg = "green" , bd = 2 , relief = SUNKEN , anchor=W).pack(side = BOTTOM , fill = X )


    label1 = Label(root , text="Enter no. of nodes : ").pack()


    #nodevalue = Spinbox(root , from_= 1 , to = 30).pack()
    nodevar = StringVar()
    nodevalue = Entry(root , textvariable = nodevar).pack()

    def getValue():
        no_of_nodes = int(nodevar.get())
        print( no_of_nodes )


    startbutton = Button(root , text = "Start" , fg="red" , command = getValue).pack()

    

    root.mainloop()


