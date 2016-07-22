from chat_window import ChatWindow
from sign_in_window import SignInWindow
from error_window import ErrorWindow
from threading import Thread
import socket

PORT = 12345
HOST = "1.53.190.110"
PACKAGE_LEN = 300
MESSAGE_LEN = 290
USERNAME_LEN = 10
CONNECTION_ERROR = "CONN_ERR"

connected = True
running = True

def clean_up():
    global thread_1, thread_2, chat_window, running

    running = False

    chat_window.cv.acquire()
    chat_window.cv.notify()
    chat_window.cv.release()

    thread_1.join()
    thread_2.join()
    chat_window.root.destroy()

    client_socket.close()

def connection_error():
    error_message = ErrorWindow("Connection lost!!!\nRestart the program!!!")
    error_message.root.mainloop()

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

def send_to_server():
    global running, connected, chat_window, client_socket

    while running and connected:
        chat_window.cv.acquire()
        while chat_window.num_queue == 0 and running == True:
            chat_window.cv.wait()

        if not running or not connected:
            return

        message = chat_window.message_queue.get()
        chat_window.num_queue -= 1

        if len(message) == 0:
            continue
        
        # Username padding
        user_name = chat_window.user_name
        while (len(user_name) < USERNAME_LEN):
            user_name = user_name + " "

        # Message padding
        message = user_name + message
        while (len(message) < PACKAGE_LEN):
            message = message + " "
        # Message sending
        error = write_bytes_to_socket(PACKAGE_LEN, client_socket, message)
        if error:
            connection_error()
            connected = False
            return

        chat_window.cv.release()

def receive_from_server():
    global running, connected, chat_window, client_socket
    
    while running and connected:
        if not running or not connected:
            return

        # Parse username
        (user_name, error) = read_bytes_from_socket(USERNAME_LEN, client_socket) 
        if error:
            connection_error()
            connected = False
            return

        # Parse message
        (message, error) = read_bytes_from_socket(MESSAGE_LEN, client_socket)
        if error:
            connection_error()
            connected = False
            return

        while user_name[len(user_name) - 1] == ' ':
            user_name = user_name[:len(user_name) - 1]
        while message[len(message) - 1] == ' ':
            message = message[:len(message) - 1]
        message = message + "\n"
        chat_window.displayChat(user_name + ": " + message)
    
sign_in_window = SignInWindow()
sign_in_window.root.mainloop()

host_name = HOST
user_name = sign_in_window.get_user_name()
port = PORT

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host_name, int(port)))

chat_window = ChatWindow(user_name)
chat_window.root.protocol("WM_DELETE_WINDOW", clean_up)

thread_1 = Thread(target = send_to_server, args = ())
thread_2 = Thread(target = receive_from_server, args = ())

thread_1.start()
thread_2.start()

chat_window.root.mainloop()




