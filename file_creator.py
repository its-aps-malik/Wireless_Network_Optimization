import plotly.graph_objects as go
import plotly
from time import *
import os
import pandas as pd


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


def write_to_xlsx(node):
    print()


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


def create_excel_file(node):
    if node.node_id == -1:
        abc = "touch /home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/sink.xlsx"
        os.system(abc)
        add_log("sink.xlsx created")
    else:
        abc = "touch /home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/node" + str(node.node_id + 1) + ".xlsx"
        os.system(abc)
        add_log("/node" + str(node.node_id + 1) + ".xlsx created")


def generated_data_to_excel(node , sheet):

    if node.node_id == -1:
        file_name = "/home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/sink.xlsx"
        for i in node.packet_list:
            ###... data to write in excel file ...###
            #node_id = 
            ###... data to write in excel file ...###
            pd.DataFrame()
            sheet = sheet

        with pd.ExcelWriter(file_name , mode = "a") as writer:
            df.write_to_xlsx(writer , sheet_name = sheet)
    else:
        file_name = "/home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/node" + str(node.node_id + 1) + ".xlsx"
        pd.DataFrame()
        sheet = sheet

        with pd.ExcelWriter(file_name , mode = "a") as writer:
            df.write_to_xlsx(writer , sheet_name = sheet)