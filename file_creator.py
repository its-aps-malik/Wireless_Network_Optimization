# this file is not yet complete...

import plotly.graph_objects as go
from update_log import *
import plotly

make_project()

plotly.io.orca.config.executable = '/usr/bin/orca'
plotly.io.orca.config.save()

fig = go.Figure(go.Sunburst(
    labels=["sink","1","2","3","4","5","6","7","8","9","10"],
    ids=["-1","0","1","2","3","4","5","6","7","8","9"],
    parents=["","2","8","5","-1","6","-1","2","5","3","5"]
))

fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
fig.write_image("/home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/network_diagram.png")
#fig.write_image("/home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/network_diagram.jpeg")
#fig.write_image("/home/anant/Desktop/Wireless_Network_Optimization_Results/" + project_name + "/network_diagram.png")

fig.show()

def create_graph(node_connection):
    print(node_connection)