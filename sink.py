from update_log import *


class Sink():
    def __init__(self, sink_id = -1, level = 0):
        self.sink_id = sink_id
        self.level = level

    def recieve_packets(self):
        print("recieving packets...")
