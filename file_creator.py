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


def on_start(data):
    add_log(data)
    print(data)


def on_finish(data):
    add_log(data)
    print(data)


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
    print("Network diagram saved at  :-  '/home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "' as 'network_diagram.html'")


def create_excel_file(node):
    if node.node_id == -1:
        abc = "touch /home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/sink.xlsx"
        os.system(abc)
        add_log("sink.xlsx created")
        print("sink.xlsx created")
    else:
        abc = "touch /home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/node" + str(node.node_id + 1) + ".xlsx"
        os.system(abc)
        add_log("node" + str(node.node_id + 1) + ".xlsx created")
        print("node" + str(node.node_id + 1) + ".xlsx created")


def generated_data_to_excel(node , sheet):
    k = True
    if node.node_id == -1:
        
        file_name = "/home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/sink.xlsx"
        stuff = dict()
        
        stuff["id"] = [node.packet_list[-1].packet_id]
        stuff["data"] = [node.packet_list[-1].data]
        stuff["priority"] = [node.packet_list[-1].priority]
        stuff["Creation_time"] = [node.packet_list[-1].gen_time]
        try :
            main_df = pd.read_excel(file_name , sheet_name=sheet)
        except :
            df = pd.DataFrame(stuff)
        
        if main_df.empty == False:
            df_curr = pd.DataFrame(stuff)
            df = main_df.append(df_curr)
        
        with pd.ExcelWriter(file_name) as writer:
            df.to_excel(writer , sheet_name = sheet , index=False)

    else:
        
        file_name = "/home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/node" + str(node.node_id + 1) + ".xlsx"
        stuff = dict()
        
        stuff["id"] = [node.packet_list[-1].packet_id]
        stuff["data"] = [node.packet_list[-1].data]
        stuff["priority"] = [node.packet_list[-1].priority]
        stuff["Creation_time"] = [node.packet_list[-1].gen_time]
        try :
            main_df = pd.read_excel(file_name , sheet_name=sheet)
        except :
            df = pd.DataFrame(stuff)
            k = False
        
        if k:
            df_curr = pd.DataFrame(stuff)
            df = main_df.append(df_curr)
        
        with pd.ExcelWriter(file_name) as writer:
            df.to_excel(writer , sheet_name = sheet , index=False)
