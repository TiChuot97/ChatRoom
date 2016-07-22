from Tkinter import *
from error_window import ErrorWindow

class SignInWindow(): 
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Sign in")
        self.root.geometry("400x30")
        self.root.resizable(width = FALSE, height = FALSE)

        """self.tag_host_name = Label(width = 50, height = 2, anchor = W, text = "Host name:", relief = SUNKEN)
        self.tag_host_name.pack(fill = X)
        self.enter_host_name = Entry(self.tag_host_name, width = 35, relief = SUNKEN)
        self.enter_host_name.pack(side = RIGHT, fill = X, padx = 2, pady = 2)
        self.enter_host_name.bind("<Return>", self.sign_in)

        self.tag_port = Label(width = 50, height = 2, anchor = W, text = "Port:", relief = SUNKEN)
        self.tag_port.pack(fill = X)
        self.enter_port = Entry(self.tag_port, width = 35, relief = SUNKEN)
        self.enter_port.pack(side = RIGHT, fill = X, padx = 2, pady = 2)
        self.enter_port.bind("<Return>", self.sign_in)"""

        self.tag_user_name = Label(width = 50, height = 2, anchor = W, text = "User name:", relief = SUNKEN)
        self.tag_user_name.pack(fill = X)
        self.enter_user_name = Entry(self.tag_user_name, width = 35, relief = SUNKEN)
        self.enter_user_name.pack(side = RIGHT, fill = X, padx = 2, pady = 2)
        self.enter_user_name.bind("<Return>", self.sign_in)

    def sign_in(self, event):
        """self.host_name = self.enter_host_name.get()
        self.enter_host_name.delete(0, END)

        self.port = self.enter_port.get()
        self.enter_port.delete(0, END)"""

        self.user_name = self.enter_user_name.get()
        self.enter_user_name.delete(0, END)

        """if self.host_name == "" or self.port == "" or self.user_name == """""

        if self.user_name == "":
            self.error_window()
        else:
            self.root.destroy()

    def error_window(self):
        error_message = ErrorWindow("Host name, port number or username is missing!!!")
        error_message.root.mainloop()

    def get_host_name(self):
        return self.host_name

    def get_port(self):
        return self.port

    def get_user_name(self):
        return self.user_name
