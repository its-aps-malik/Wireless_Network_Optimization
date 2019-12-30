class Sink():
    def __init__(self, sink_id = 0, level = 0):
        self.sink_id = sink_id
        self.level = level

    def recieve_packets(self):
        print("recieving packets...")
