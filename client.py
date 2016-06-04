import chat_window
from Tkinter import *

host_name = ""
port = ""
user_name = ""
    
class SignInWindow(): 
    
    def __init__(self):

        self.root = Tk()
        self.root.title("Sign in")
        self.root.geometry("400x100")
        self.root.resizable(width = FALSE, height = FALSE)

        self.tag_host_name = Label(width = 50, height = 2, anchor = W, text = "Host name:", relief = SUNKEN)
        self.tag_host_name.pack(fill = X)
        self.enter_host_name = Entry(self.tag_host_name, width = 35, relief = SUNKEN)
        self.enter_host_name.pack(side = RIGHT, fill = X, padx = 2, pady = 2)
        self.enter_host_name.bind("<Return>", sign_in)

        self.tag_port = Label(width = 50, height = 2, anchor = W, text = "Port:", relief = SUNKEN)
        self.tag_port.pack(fill = X)
        self.enter_port = Entry(self.tag_port, width = 35, relief = SUNKEN)
        self.enter_port.pack(side = RIGHT, fill = X, padx = 2, pady = 2)
        self.enter_port.bind("<Return>", sign_in)

        self.tag_user_name = Label(width = 50, height = 2, anchor = W, text = "User name:", relief = SUNKEN)
        self.tag_user_name.pack(fill = X)
        self.enter_user_name = Entry(self.tag_user_name, width = 35, relief = SUNKEN)
        self.enter_user_name.pack(side = RIGHT, fill = X, padx = 2, pady = 2)
        self.enter_user_name.bind("<Return>", sign_in)

        self.root.mainloop()
    
    def sign_in(self, event):

    self.host_name = enter_host_name.get()
    self.enter_host_name.delete(0, END)

    self.port = enter_port.get()
    self.enter_port.delete(0, END)

    self.user_name = enter_user_name.get()
    self.enter_user_name.delete(0, END)

    if self.host_name == "" or self.port == "" or self.user_name == "":
        error_window()
    else:
        tag_host_name.destroy()
        enter_host_name.destroy()
        tag_port.destroy()
        enter_port.destroy()
        tag_user_name.destroy()
        enter_user_name.destroy()
        root.destroy()

def error_window():
    error_root = Tk()
    error_root.title("Error!!!")
    error_root.geometry("400x50")
    error_root.resizable(width = FALSE, height = FALSE)

    error_message = Label(error_root, width = 400, height = 100,
            text = "Host name, port number or username is missing!!!")
    error_message.pack()

    error_root.mainloop()

sign_in_window()
print host_name, port, user_name

