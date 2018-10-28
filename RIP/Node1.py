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

class Node1:

    def __init__(self, id):
        self.id = id
        self.nodes = []

    def rinit1(self):
        self.nodes.insert(0, 1)
        self.nodes.insert(1, 0)
        self.nodes.insert(2, 1)
        self.nodes.insert(3, 999)
        self.tolayer2()

    def tolayer2(self):
        print 'enviando custos para os vizinhos...'

    def rupdate1(self, package):
        print 'atualizando custos...'

    def printdt1(self):
        for i in xrange(0, len(self.nodes)):
            print 'distancia do node 0 ate o node ', i, ' eh de ', self.nodes[i]

def receiver_thread():
    while True:


    # Main
def main():
    # receiver_thread
    node = Node1(1)
    node.rinit1()
    node.printdt1()

if __name__ == "__main__":
    sys.exit(main())
