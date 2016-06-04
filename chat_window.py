from Tkinter import *

class ChatWindow(object):

    def __init__(self):
        self.root = Tk()

        self.users_frame = Frame(width = 150, bg = "black", relief = SUNKEN)
        self.users_frame.pack(side = LEFT, fill = Y, padx = 2, pady = 2)

        self.message_box = Text(fg = "black", bg = "yellow", relief = SUNKEN, state = DISABLED)
        self.message_box.pack(fill = BOTH, expand = 1, padx = 2, pady = 2)

        self.chat_box = Text(height = 5, bg = "red", relief = SUNKEN)
        self.chat_box.pack(fill = X, padx = 2, pady = 2)
        self.chat_box.bind("<Return>", self.sendChat)

        self.send_button = Button(self.chat_box, height = 5, width = 7, fg = "red", bg = "black",
                                  text = "SEND", relief = SUNKEN, command = self.receiveChat)
        self.send_button.pack(side = RIGHT, padx = 2, pady = 2)

    def receiveChat(self):
        message = self.chat_box.get(1.0, END)
        self.chat_box.delete(1.0, END)
        return message

    def displayChat(self, message):
        self.message_box.config(state = NORMAL)
        self.message_box.insert(END, message)
        self.message_box.see(END)
        self.message_box.config(state = DISABLED)

    def sendChat(self, event):
        self.receiveChat();
        
