import plotly.graph_objects as go
import plotly
from time import *
import os


###... (    ALL VARIABLES ARE DEFINED BELOW    ) ...###

project_name = str(time()).split('.')[0]
log_file_name = "/home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/logs.txt"

###... (    ALL VARIABLES ARE DEFINED ABOVE    ) ...###


def make_project():
    os.system("mkdir -p ~/Desktop/Wireless_Network_Optimization_Results/" + project_name)
    dir_notification = "Directory created  :-  ~/Desktop/Wireless_Network_Optimization_Results/" + project_name
    print(dir_notification)

    os.system("touch " + log_file_name)
    log_notification = " File created  :-  /home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/logs.txt"
    print(log_notification)

    on_start(dir_notification)
    on_start(log_notification)


def add_log(data):
    c_time = ctime()
    log_file = open(log_file_name , 'a')
    log_file.writelines("\n" + str(c_time) + " - " + str(time()) + " - " + data + "\n")
    log_file.flush()
    log_file.close()


def on_start(data):
    add_log(data)


def on_finish(data):
    add_log(data)


def create_graph(node_connection_list):
    
    name_of_nodes = ["sink"]
    id_of_nodes = ["-1"]
    parent_of_node = [""]

    for i in range(len(node_connection_list)):
        name_of_nodes.append("node-" + str(node_connection_list[i][0][0] + 1) )
        id_of_nodes.append(str(node_connection_list[i][0][0]))
        parent_of_node.append(str(node_connection_list[i][1][0]))

    fig = go.Figure(go.Sunburst(
        labels = name_of_nodes,
        ids = id_of_nodes,
        parents = parent_of_node
    ))

    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

    fig.write_html("/home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/network_diagram.html")
    add_log("Network diagram saved at  :-  '/home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "' as 'network_diagram.html'")

