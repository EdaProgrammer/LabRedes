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

class Node3:

    def __init__(self, id):
        self.id = id
        self.nodes = []

    def rinit3(self):
        self.nodes.insert(0, 7)
        self.nodes.insert(1, 999)
        self.nodes.insert(2, 2)
        self.nodes.insert(3, 0)
        self.tolayer2()

    def tolayer2(self):
        print 'enviando custos para os vizinhos...'

    def rupdate3(self, package):
        print 'atualizando custos...'

    def printdt3(self):
        for i in xrange(0, len(self.nodes)):
            print 'distancia do node 0 ate o node ', i, ' eh de ', self.nodes[i]

def receiver_thread():
    while True:


    # Main
def main():
    # receiver_thread
    node = Node3(0)
    node.rinit3()
    node.printdt3()

if __name__ == "__main__":
    sys.exit(main())
