import socket

class El_gamal_client:
    def __init__(self):
        self.__sockets = []
        self.__keys = []
        self.__times = []

    def new_socket(self, ip: str, port: int):
        try:
            socket_ = socket.socket()
            socket_.connect((ip, port))
            self.__sockets.append(socket_)
        except:
            print("Error")

    def get_sockets(self):
        return self.__sockets

    def get_keys(self):
        return self.__keys

    def get_times(self):
        return self.__times

    def distributed_key(self, bits: int, iterations: int):
        for _ in range(iterations):
            _key = []
            _time = []

            for socket_ in self.get_sockets():
                socket_.send(str(bits).encode())

            for socket_ in self.get_sockets():
                message = socket_.recv(8192).decode().split(";")
                _key.append(message[0])
                _time.append(message[1])

            self.get_keys().append(_key)
            self.get_times().append(_time)

    def terminate(self):
        for socket_ in self.get_sockets():
            socket_.send("end".encode())
            socket_.close()

socket_atual = El_gamal_client()

socket_atual.new_socket(ip='192.168.1.111',port=13134)
socket_atual.distributed_key(161,3)
socket_atual.terminate()
print(socket_atual.get_times())



