from file_creator import data_to_excel

class Sink():
    def __init__(self, node_id = -1, r_energy = 0, level = 0 ):
        self.node_id = node_id
        self.r_energy = r_energy
        self.level = level
        self.buffer = []

    def set_r_energy(self, energy):# sets recieving energy value
        self.r_energy = energy
    
    def get_r_energy(self):# returns recieving energy value
        return(self.r_energy)

    def recieve_packet(self, data, node, algo):# this method is initiated whenever a node sends data to sink node
        data_to_excel(self, data, algo+"-recieved")
        self.buffer.append(data)
        self.set_r_energy(energy=0)
        print("data recieved from node " + str(node.node_id))
