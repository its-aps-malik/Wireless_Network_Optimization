from threading import *
from time import *
from random import *
from update_log import *


###... (    ALL VARIABLES ARE DEFINED BELOW    ) ...###
node_list = []
temp_node_list = []
network_list = []
connected_nodes = []
###... (    ALL VARIABLES ARE DEFINED ABOVE    ) ...###


class Nodes(Thread):
    def __init__(self, node_id, level = 999, r_energy = 0, s_energy = 0, packets_to_send = 100, node_to_send = None, connected_nodes = []):   # this is init method
        Thread.__init__(self)
        self.node_id = node_id
        self.level = level
        self.r_energy = r_energy
        self.s_energy = s_energy
        self.packets_to_send = packets_to_send
        self.node_to_send = node_to_send
        self.connected_nodes = connected_nodes

    def run (self):  #this methos is executed when a thread is started
        flag=True
        print(str(self.node_id) + " started")
        i=0
        while flag :
            print (self.node_id, end=" ")
            i=i+1
            sleep(0.1)
            if i > 10:
                i=0
                flag= False

    def get_node_id(self):
        return(self.node_id)

    def set_r_energy(self, energy):# this method sets node's recieving energy value
        self.r_energy = energy

    def set_s_energy(self, energy):# this method sets node's sending energy value
        self.s_energy = energy

    def get_r_energy(self):# this method returns node's recieving energy value
        return(self.r_energy)

    def get_s_energy(self):# this method returns node's sending energy value
        return(self.s_energy)

    def get_packets_to_send(self):# this method returns total no of packets remaining that a node needs to send
        return(self.packets_to_send)

    def get_connected_nodes(self):# this method returns all connected nodes
        return(self.connected_nodes)

    def set_rx_node(self):
        print("rx_node calculated here...")
    
    def send_packet(self, rx_node):
        print("send data here to " + str(rx_node))

    def recieve_packets(self):
        print("recieving packets...")

def create_network_tree(total_nodes):

    temp_node_list = node_list.copy()
    random_from_node_list = None
    random_from_network_list = None
    
    for i in range(total_nodes):
        random_from_node_list = temp_node_list.pop(randint(0,(total_nodes-1)-i))
        random_from_network_list = network_list[randint(0,(i))]
        random_from_node_list.level = random_from_network_list.level + 1
        if random_from_network_list.level == 0:
            connected_nodes.append( ( [random_from_node_list.node_id , random_from_node_list.level] , [random_from_network_list.sink_id , random_from_network_list.level] ) )
        else:
            connected_nodes.append( ( [random_from_node_list.node_id , random_from_node_list.level] , [random_from_network_list.node_id , random_from_network_list.level] ) )

        network_list.append(random_from_node_list)
    

    for i in range(len(connected_nodes)):
        print(connected_nodes[i]) 

    add_log("Network created")
    