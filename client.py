from chat_window import ChatWindow
from sign_in_window import SignInWindow
from error_window import ErrorWindow
from threading import Thread
import socket


PACKAGE_LEN = 300
MESSAGE_LEN = 290
USERNAME_LEN = 10

connection = True
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

def connection_error():
    error_message = ErrorWindow("Connection lost!!!\nRestart the program!!!")
    temp_thread = Thread(target = clean_up, args = ())
    temp_thread.join()

def send_to_server(chat_window):
    global running, connection

    while running and connection:
        chat_window.cv.acquire()
        while chat_window.num_queue == 0 and running == True:
            chat_window.cv.wait()

        if not running or not connection:
            return

        message = chat_window.message_queue.get()
        chat_window.num_queue -= 1
        
        # Username padding
        user_name = chat_window.user_name
        while (len(user_name) < USERNAME_LEN):
            user_name = user_name + " "

        # Message padding
        message = user_name + message
        while (len(message) < MESSAGE_LEN):
            message = message + " "

        # Message sending
        byte_sent = 0
        while (byte_sent < PACKAGE_LEN):
            sent = client_socket.send(message[byte_sent:])
            if sent == 0:
                connection_error()
                connection = False
                return
            byte_sent += sent

        chat_window.cv.release()

def receive_from_server():
    global running, connection
    
    while running and connection:
        byte_read = 0
        package = ""
        if not running or connection:
            return
        while byte_read < PACKAGE_LEN:
            piece = client_socket.recv(PACKAGE_LEN - byte_read)
            if len(piece) == 0:
                connection_error()
                connection = False
                return
            package = package + piece
            byte_read += len(piece)
    
sign_in_window = SignInWindow()
sign_in_window.root.mainloop()

host_name = sign_in_window.get_host_name()
user_name = sign_in_window.get_user_name()
port = sign_in_window.get_port()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host_name, int(port)))

chat_window = ChatWindow(user_name)
chat_window.root.protocol("WM_DELETE_WINDOW", clean_up)

thread_1 = Thread(target = send_to_server, args = (chat_window, ))
thread_2 = Thread(target = receive_from_server, args = ())

thread_1.start()
thread_2.start()

chat_window.root.mainloop()




