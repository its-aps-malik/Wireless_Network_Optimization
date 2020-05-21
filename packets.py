from random import random , choice
from time import time

class Packet:
    def __init__(self, gen_time = None):
        self.packet_id = 'pkt_'+str(time())
        self.data = 'temp° - '+str(random()*100)
        self.priority = choice([0,0,0,0,0,0,0,0,0,0,1,1,1,2,2])
        self.time_out = 5.0
        self.gen_time = gen_time

    def set_gen_time(self,val):
        self.gen_time = val

    def get_gen_time(self):
        return(self.gen_time)