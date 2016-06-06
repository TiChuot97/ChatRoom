from Tkinter import *
from multiprocessing import Queue
import threading

class ChatWindow(object):

    def __init__(self, user_name):
        self.root = Tk()
        self.root.title("Welcome to USG_Chatroom")

        self.users_frame = Frame(width = 150, bg = "black", relief = SUNKEN)
        self.users_frame.pack(side = LEFT, fill = Y, padx = 2, pady = 2)

        self.message_box = Text(fg = "black", bg = "yellow", relief = SUNKEN, state = DISABLED)
        self.message_box.pack(fill = BOTH, expand = 1, padx = 2, pady = 2)

        self.chat_frame = Frame(height = 2, relief = SUNKEN, bg = "blue")
        self.chat_frame.pack(fill = X, padx = 2, pady = 2)

        self.chat_box = Entry(self.chat_frame, bg = "red", relief = SUNKEN)
        self.chat_box.pack(fill = X, side = LEFT, expand = True)
        self.chat_box.bind("<Return>", self.sendChat)

        self.send_button = Button(self.chat_frame, width = 7, fg = "red", bg = "black",
                                  text = "SEND", relief = SUNKEN, command = self.receiveChat)
        self.send_button.pack(fill = Y, side = LEFT)

        self.message_queue = Queue()
        self.num_queue = 0

        self.cv = threading.Condition()

        self.user_name = user_name

    def receiveChat(self):
        message = self.chat_box.get()
        self.chat_box.delete(0, END)
        self.message_queue.put(message)
        self.num_queue += 1
        self.cv.acquire()
        self.cv.notify()
        self.cv.release()

    def displayChat(self, message):
        self.message_box.config(state = NORMAL)
        self.message_box.insert(END, self.user_name + ": " + message + "\n")
        self.message_box.see(END)
        self.message_box.config(state = DISABLED)

    def sendChat(self, event):
        self.receiveChat();

