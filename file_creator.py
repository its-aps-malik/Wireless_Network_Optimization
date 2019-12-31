import plotly.graph_objects as go
from update_log import *
import plotly


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
