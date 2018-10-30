# ----------- R I P -------------- #

# Gustavo da Silva Eda 620114
# Renan

from random import *
import socket
import thread
import pickle
import sys
import signal
import time
import Packet
import RIPTableElement

class Node0:

    def __init__(self, id):
        self.id = id
        self.table = []

    # guardar antecessor
    def rinit0(self):
        self.table.append(RIPTableElement(0, 0))
        self.table.append(RIPTableElement(1, 0))
        self.table.append(RIPTableElement(3, 0))
        self.table.append(RIPTableElement(7, 0))

        for i in range(1, 4):
            p = Packet(0, i, self.table)
            self.tolayer2(p)

    def tolayer2(self, packet):
        print 'enviando custos para os vizinhos...'
        # abre socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(localhost, 3000 + packet.dest)
        s.send(pickle.dumps(packet))

    def rupdate0(self, packet):
        print 'atualizando custos...'

    def printdt0(self):
        for i in xrange(0, len(self.nodes)):
            print 'distancia do node 0 ate o node ', i, ' eh de ', self.nodes[i]

    def send_routine_packet(self, dest):
        pacote = Packet(self.id, self.table)

# def receiver_thread():
#     while True:


    # Main
def main():
    # receiver_thread
    node = Node0(0)
    node.rinit0()
    node.printdt0()

if __name__ == "__main__":
    sys.exit(main())
