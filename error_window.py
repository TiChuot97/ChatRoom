from Tkinter import *

class ErrorWindow(object):

    def __init__(self, error_message):
        self.root = Tk()
        self.root.title("Error!!!")
        self.root.geometry("400x50")
        self.root.resizable(width = FALSE, height = FALSE)

        self.error_message = Label(self.root, width = 400, height = 100,
                text = error_message) 
        self.error_message.pack()

