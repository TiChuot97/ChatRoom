# coding: utf-8
import socket
import Queue
import threading
from threading import Thread
import sys

PORT = 12345
PACKAGE_LEN = 300
MESSAGE_LEN = 290
USERNAME_LEN = 10
MAX_CLIENTS = 100
CONNECTION_ERROR = "CONN_ERR"

def write_bytes_to_socket(num_bytes, socket, message):
    bytes_sent = 0
    while bytes_sent < num_bytes:
        sent = socket.send(message[bytes_sent:])
        if sent == 0:
            return True
        bytes_sent += sent
    return False

def read_bytes_from_socket(num_bytes, socket):
    bytes_read = 0
    package = ""
    while bytes_read < num_bytes:
        piece = socket.recv(num_bytes - bytes_read)
        if len(piece) == 0:
            return (CONNECTION_ERROR, True)
        package = package + piece
        bytes_read += len(piece)
    return (package, False)

def process_client(client_socket, num_client):
    global queue
    while True:
        (package, error) = read_bytes_from_socket(PACKAGE_LEN, client_socket)
        if error:
            break
        queue.put(package)
        cv.acquire()
        cv.notify()
        cv.release()
    client_connected[num_client] = 0

def send_messages():
    global queue, cv
    while True:
        cv.acquire()
        while queue.empty():
            cv.wait()
        cv.release() 
        package = queue.get()
        for (sock, num) in client_sockets:
            write_bytes_to_socket(PACKAGE_LEN, sock, package)

port = PORT

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((socket.gethostname(), port))

server_socket.listen(5)

queue = Queue.Queue()

cv = threading.Condition()

num_clients = 0

client_sockets = []

client_connected = [1 for x in range(101)]

while True:
    (client_socket, address) = server_socket.accept()
    new_thread = Thread(target = send_messages, args = ())
    new_thread.setDaemon(True)
    new_thread.start()
    if num_clients == MAX_CLIENTS:
        client_socket.close() 
    else:
        new_thread = Thread(target = process_client, args = (client_socket, num_clients + 1))
        new_thread.setDaemon(True)
        new_thread.start()
        num_clients += 1
        client_sockets.append((client_socket, num_clients))


