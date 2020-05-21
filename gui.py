from tkinter import Tk , Menu , Label , StringVar , Entry , Button , SUNKEN , BOTTOM , W , X
from sink import Sink
from nodes import network_list , node_list
from nodes import Nodes , create_network_tree
from file_creator import  data_to_excel #, create_excel_file
from packets import Packet

# from nodes import *
# from sink import *
# from file_creator import *


###... (    ALL VARIABLES ARE DEFINED BELOW    ) ...###
no_of_nodes = 0
###... (    ALL VARIABLES ARE DEFINED ABOVE    ) ...###


def changeLater():
    print("lol")

def loadUI():

    root = Tk(screenName=":0")# will display in screen 1 in case of multiple moniter setup


    root.title("Wireless Netework Simulator")# \
    root.geometry("800x600")                 # |- sets title , window size and disables resizability
    root.resizable(0, 0)                     # /

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

    status_notification = Label(root , text="Progress bar to be placed here..." , bg = "green" , bd = 2 , relief = SUNKEN , anchor=W)
    status_notification.pack(side = BOTTOM , fill = X)

    label1 = Label(root , text="Enter no. of nodes : ")
    label1.pack()

    nodevar = StringVar()
    nodevalue = Entry(root , textvariable = nodevar)
    nodevalue.pack()

    def getValue():
        # creating and adding sink to network list
        network_list.append(Sink())
        
        # # creating excel files for each node
        # for i in network_list:
        #     create_excel_file(i)

        # creating nodes and genetating data
        no_of_nodes = int(nodevar.get())
        for i in range (no_of_nodes):
            node_list.append(Nodes(i))
            for j in range(10):
                packet = Packet()
                node_list[-1].packet_list.append(packet)
                data_to_excel(node_list[-1], node_list[-1].packet_list[-1], 'generated_data')

        # creating random network
        create_network_tree(no_of_nodes)

        # starting node threads
        for i in node_list:
            i.start()


    startbutton = Button(root , text = "Start" , fg="red" , command = getValue)
    startbutton.pack()


    root.mainloop()