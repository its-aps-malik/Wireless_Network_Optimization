from threading import Thread
from collections import deque
from random import randint
from file_creator import add_log , create_graph , data_to_excel
from time import sleep


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
        self.packet_list = []
        self.fcfs_buffer = deque()
        self.buffer_0 = deque()
        self.buffer_1 = deque()
        self.buffer_2 = deque()

    def run (self):  #this method is executed when a thread is started
                
        add_log("Node " + str(self.node_id) + " started")
        print("Node " + str(self.node_id) + " started")

        # transfering data from packet_list to fcfs_buffer
        for i in range(len(self.packet_list)):
            self.fcfs_buffer.append(self.packet_list[i])

        self.fcfs_transfer()

        print("node-"+str(self.node_id)+" stopped...")



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


    def set_rx_node(self, node):# this node sets the node to which data is to be send by current node
        self.node_to_send = node
    

    def recieve_packet(self, data, node, algo):# this method is initiated whenever a node sends data to another node
        data_to_excel(self, data, algo+"-recieved")
        self.fcfs_buffer.append(data)
        self.set_r_energy(energy=0)
        print("data recieved from node " + str(node.node_id))


    def send_packet(self, data, algo):# this method trys to send data to next node untill it is successfully sent
        flag = True
        while(flag):
            if(self.node_to_send.get_r_energy() == 0):
                print("node "+str(self.node_id)+" sending data to " + str(self.node_to_send.node_id))
                data_to_excel(self, data, algo+"-send")
                self.node_to_send.set_r_energy(energy=1)
                self.node_to_send.recieve_packet(data, self, algo)
                sleep(1)
                flag=False
            else:
                sleep_val = randint(1, 5)
                print("receiving node busy - trying after "+str(sleep_val)+" seconds...")
                sleep(sleep_val)
        return "success"


    def fcfs_transfer(self):# this method uses FCSF to transfer data
        print("\n\ndata transfer via FCFS started...\n\n")

        while(len(self.fcfs_buffer)!=0):
                status = self.send_packet(self.fcfs_buffer[-1], "FCFS")
                if(status == "success"):
                    self.fcfs_buffer.pop()

        print("\n\ndata transfer via FCFS completed...\n\n")

    
    def selective_drop_transfer(self):# this method uses Selective Drop to transfer data
        print("lol")

    


def create_network_tree(total_nodes):# this node creates the random network during each run

    temp_node_list = node_list.copy()
    random_from_node_list = None
    random_from_network_list = None
    
    for i in range(total_nodes):

        random_from_node_list = temp_node_list.pop(randint(0,(total_nodes-1)-i))
        random_from_network_list = network_list[randint(0,(i))]
        random_from_node_list.level = random_from_network_list.level + 1
        random_from_node_list.set_rx_node(random_from_network_list)        
        connected_nodes.append( ( [random_from_node_list.node_id , random_from_node_list.level] , [random_from_network_list.node_id , random_from_network_list.level] ) )
        network_list.append(random_from_node_list)
    

    add_log("Network created")
    print("Network created")

    create_graph(connected_nodes)