import socket
import time
from Crypto import Random
from Crypto.PublicKey import ElGamal

class El_gamal_server:
    def __init__(self):
        self.__socket = None
        self.__client = None

    def new_socket(self, ip: str, port: int):
        try:
            socket_ = socket.socket()
            socket_.bind((ip, port))
            self.__socket = socket_
        except:
            print("Error")

    def get_socket(self):
        return self.__socket

    def get_client(self):
        return self.__client

    def set_client(self, client):
        self.__client = client

    def terminate(self):
        self.get_socket().close()
        self.get_client().close()

    def encryptionKey(self,bits:int):
        return ElGamal.generate(bits, Random.new().read)

    def __get_key__(self, bits:int):
        start_time = time.time()
        key = self.encryptionKey(bits)
        end_time = time.time()
        return key, (end_time-start_time)

    def run(self, n_listen = 10):
        self.get_socket().listen(n_listen)
        while True:
            if self.get_client() == None:
                client_aux, addr = self.get_socket().accept()
                self.set_client(client_aux)
                print("Cliente conectado", addr)

            content = self.get_client().recv(8192).decode()
            print(content, content.__class__)
            if content == "end":
                self.terminate()
                break
            else:
                key, delta_time = self.__get_key__(int(content))
                self.get_client().send((str([key.p, key.g, key.x, key.y])+";"+str(delta_time)).encode('UTF-8'))

server = El_gamal_server()
server.new_socket(ip="192.168.1.111",port=13134)
server.run()
