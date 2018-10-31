# ----------- R I P -------------- #

# Gustavo da Silva Eda          620114
# Renan Rossignatti de Franca   489697

from RIPTableElement import RIPTableElement
from Packet import Packet
from random import *
import socket
import thread
import pickle
import sys
import signal
import time

class Node:

    def __init__(self):
        self.id = 0
        self.neighbours = [1, 2, 3]
        self.paths = [] # RIPTableElements

    # guardar antecessor
    def rinit(self):
        self.paths.append(RIPTableElement(0, self.id))
        self.paths.append(RIPTableElement(1, self.id))
        self.paths.append(RIPTableElement(3, self.id))
        self.paths.append(RIPTableElement(7, self.id))

        print 'enviando custos para os vizinhos...'
        for i in self.neighbours:
            p = Packet(self.id, i, self.paths)
            self.tolayer2(p)

    def tolayer2(self, packet):
        # abre socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 3000 + packet.dest)
        s.connect(server_address)
        s.send(pickle.dumps(packet))

    def rtupdate(self, packet):
        flag_update = False

        print 'atualizando custos...'
        for i in xrange(len(packet.paths)):
            # ignora custo do vizinho a ele mesmo
            if i == packet.source:
                continue

            combined_cost = self.paths[packet.source].cost + packet.paths[i].cost

            # se o no ainda nao foi descoberto
            if self.paths[i].cost == -1 or combined_cost < self.paths[i].cost:
                flag_update = True
                self.paths[i].cost = combined_cost
                self.paths[i].antecessor = packet.source

        if flag_update:
            print 'enviando novos custos para os vizinhos...'
            for i in self.neighbours:
                p = Packet(self.id, i, self.paths)
                self.tolayer2(p)
            self.printdt()


    def printdt(self):
        for i in xrange(len(self.paths)):
            print 'distancia do node ', self.id ,' ate o node ', i, ' eh de ', self.paths[i].cost



def receiver_thread():
    while True:
        # cria socket
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # liga a uma porta
        serverSocket.bind(('',3000 + node.id))
        # tamanho da fila
        serverSocket.listen(5)


        while True:
            time.sleep(5)
            node.rinit()
            (clientSocket, address) = serverSocket.accept()

            try:
                data = clientSocket.recv(1024)
                pkt = pickle.loads(data)
                node.rtupdate(pkt)
            except Exception as e:
                print 'Erro no recebimento:', e

# Main
def main():
    global node
    node = Node()

    # receiver_thread
    thread.start_new_thread(receiver_thread, ())

    signal.pause()

if __name__ == "__main__":
    sys.exit(main())
