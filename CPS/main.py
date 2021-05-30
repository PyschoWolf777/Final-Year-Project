from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as mb

class Login:
    def __init__(self, root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+0+50")
        #=========== BG Image ================

        self.bg=ImageTk.PhotoImage(file="lcd.jpg")
        self.bgImage = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight = 1)

        self.root.resizable(False, False)

        #=========== Login Frame =============

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=150, y=120, height = 400, width = 500)


        title = Label(Frame_login, text = "Login Here", font = ("Impact", 35, "bold"), fg = "#097179", bg = "white").place(x = 140, y = 30)
        desc = Label(Frame_login, text="Accountant Employee Login Area", font=("Goudy old style", 15, "bold"), fg="#097179", bg="white").place(
            x=100, y=100)

        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"),
                     fg="gray", bg="white").place(x=100, y=140)

        self.txt_user = Entry(Frame_login, font = ("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=100, y=170, width = 350, height = 35)

        lbl_pass = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"),
                         fg="gray", bg="white").place(x=100, y=210)

        self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="lightgray", show = "*")
        self.txt_pass.place(x=100, y=240, width=350, height=35)

        #============= RADIO BUTTON =====================

        self.var = IntVar()
        self.var.set(1)
        lbl_pass = Label(Frame_login, text="Type", font=("Goudy old style", 15, "bold"),
                         fg="gray", bg="white").place(x=100, y=280)

        radio = Radiobutton(Frame_login, text="Higher", cursor = "hand2",variable=self.var, value=1, font=("Goudy old style", 15, "bold"),
                         fg="gray", bg="white").place (x = 250, y = 280)
        radio = Radiobutton(Frame_login, text="Lower", cursor = "hand2",variable=self.var, value=2, font=("Goudy old style", 15, "bold"),
                         fg="gray", bg="white").place(x = 370, y = 280)

        #bd = 0 means border = 0 which means that there will be no border
        forgetButton=Button(Frame_login, text="Forget Password?", cursor = "hand2",bg = "white", bd = 0,fg = "#097179",font=("times new roman", 12)).place(x=100, y = 330)

        loginButton = Button(Frame_login, text="Login", fg="white", bg="#097179", cursor = "hand2",
                        font=("times new roman", 20)).place(x=350, y=330, width = 100, height = 35)

    def login_function(self):
        if self.txt_user.get() == "" or self.txt_pass.get() == "":
            mb.showerror("Error", "All Fields are Required", parent = self.root)
        elif self.txt_user.get() != "Hamza" or self.txt_pass.get() != "abc123":
            mb.showerror("Error", "Invalid username or password", parent=self.root)
        else:
            mb.showinfo("Welcome", "Hamza ! Welcome to your home page", parent = self.root)
root = Tk()

obj = Login(root)

root.mainloop()