from file_creator import *


class Sink():
    def __init__(self, node_id = -1, r_energy = 0, level = 0):
        self.node_id = node_id
        self.r_energy = r_energy
        self.level = level

    def set_r_energy(self, energy):
        self.r_energy = energy
    
    def get_r_energy(self, energy):
        return(r_energy)

    def recieve_packets(self):
        print("recieving packets...")
