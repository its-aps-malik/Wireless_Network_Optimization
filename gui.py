from tkinter import *
import os
from nodes import *
from sink import *
from file_creator import *


###... (    ALL VARIABLES ARE DEFINED BELOW    ) ...###
no_of_nodes = 0
###... (    ALL VARIABLES ARE DEFINED ABOVE    ) ...###



def changeLater():
    print("lol")


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

    nodevar = StringVar()
    nodevalue = Entry(root , textvariable = nodevar).pack()

    def getValue():
        # creating and adding sink to network list
        network_list.append(Sink())
        
        # creating nodes
        no_of_nodes = int(nodevar.get())
        for i in range (no_of_nodes):
            node_list.append(Nodes(i))

        # creating random network
        create_network_tree(no_of_nodes)

        # starting node threads
        for i in node_list:
            i.start()


    startbutton = Button(root , text = "Start" , fg="red" , command = getValue).pack()


    root.mainloop()