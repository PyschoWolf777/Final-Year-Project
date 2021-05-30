from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as mb


class ChangeInformation:
    def __init__(self, root):
        self.root = root
        self.root.title("Floor Manager Panel")
        self.root.geometry("1199x600+0+50")

        self.root.resizable(False, False)
        # =========== Setting  Frames ================

        mainFrame = Frame(self.root, bg="white").place(width=1199, height=600)

        upperFrame = Frame(mainFrame, bg="#097179").place(x=0, y=0, width=1199, height=100)

        sideFrame = Frame(mainFrame, bg="#097179").place(x=0, y=100, width=200, height=500)

        bodyFrame = Frame(mainFrame, bg="#097179").place(x=200, y=100, width=999, height=500)

        # =============================================================================================
        # --------------------------- UPPER FRAME -----------------------------------------------------
        # =============================================================================================
        # ================ Add image logo image to the upper frame

        self.photo = PhotoImage(
            file='logo.png')  # this command will get the photo from your project, for showing it on GUI, first add this into label
        self.lbl = Label(upperFrame, image=self.photo)
        self.lbl.place(x=10, y=10, width=150, height=80)

        # ================== TITLE
        title = Label(upperFrame, text="CORONA PREVENTION SYSTEM", font=("Impact", 35, "bold"), fg="white",
                      bg="#097179").place(
            x=200, y=20)

        # =============== WELCOME The USER

        welcomeLabel = Label(upperFrame, text="Welcome!", font=("Impact", 20, "bold"), fg="white", bg="#097179").place(
            x=950, y=15)
        userNameLabel = Label(upperFrame, text="Zulqarnain", font=("Impact", 15), fg="white", bg="#097179").place(
            x=950, y=55)
        # ================= Drop Down Arrow button
        self.downButtonPhoto = PhotoImage(file="logout.png", width=40, height=40)
        self.downButton = Label(upperFrame, image=self.downButtonPhoto)
        # self.downButton.place(x=1000, y=10, width= 50, height=50)

        # HERE COMMAND IS TO BE ADDED
        # dropButton = Button(upperFrame, image = self.downButtonPhoto, cursor = "hand2", bg = "red").place(x=1130, y=30, width= 40, height=40)
        dropButton = Button(upperFrame, text="Logout", cursor="hand2", fg="white", bg="#097179",
                            font=("Times new roman", 12, "bold"), bd=3, relief=SUNKEN, command = self.logoutFunction).place(x=1100, y=30,
                                                                                             width=70, height=50)

        # =============================================================================================
        # --------------------------- SIDE FRAME -----------------------------------------------------
        # =============================================================================================

        notificationsButton = Button(sideFrame, text="Notifications", cursor="hand2", bg="#097179", bd=0, fg="white",
                             font=("times new roman", 20, "bold")).place(x=0, y=100, width=200, height=100)

        notificationsButton = Button(sideFrame, text="Violations", cursor="hand2", bg="#097179", bd=0, fg="white",
                                 font=("times new roman", 20, "bold")).place(x=0, y=200, width=200, height=100)

        notificationsButton = Button(sideFrame, text="Record", cursor="hand2", bg="#097179", bd=0, fg="white",
                               font=("times new roman", 20, "bold")).place(x=0, y=300, width=200, height=100)

        recordButton = Button(sideFrame, text="Contact Admin", cursor="hand2", bg="#097179", bd=0, fg="white",
                              font=("times new roman", 20, "bold")).place(x=0, y=400, width=200, height=100)

        changeUserButton = Button(sideFrame, text="Change info", cursor="hand2", bg="#097179", bd=0, fg="white",
                                  font=("times new roman", 20, "bold")).place(x=0, y=500, width=200, height=100)

        # =============================================================================================
        # --------------------------- Body FRAME -----------------------------------------------------
        # =============================================================================================

        # =============================== FLOOR FRAME =============================================
        addManagerFrame = Frame(bodyFrame, bg="#04c0cf").place(x=200, y=100, width=999, height=500);

        self.email = Label(addManagerFrame, text="E-mail ", bg="#04c0cf", fg="#097179",
                           font=("Helvetica", 20, "bold")).place(x=300, y=120, width=200, height=80)
        self.txt_email = Entry(addManagerFrame, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=550, y=140, width=350, height=35)

        self.phone = Label(addManagerFrame, text="Phone ", bg="#04c0cf", fg="#097179",
                           font=("Helvetica", 20, "bold")).place(x=300, y=190, width=200, height=80)
        self.txt_phone = Entry(addManagerFrame, font=("times new roman", 15), bg="lightgray")
        self.txt_phone.place(x=550, y=210, width=350, height=35)

        self.pass1 = Label(addManagerFrame, text="Password ", bg="#04c0cf", fg="#097179",
                           font=("Helvetica", 20, "bold")).place(x=300, y=260, width=200, height=80)
        self.txt_pass1 = Entry(addManagerFrame, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_pass1.place(x=550, y=280, width=350, height=35)

        self.pass2 = Label(addManagerFrame, text="Re-Enter password ", bg="#04c0cf", fg="#097179",
                           font=("Helvetica", 20, "bold")).place(x=250, y=330, width=300, height=80)
        self.txt_pass2 = Entry(addManagerFrame, font=("times new roman", 15), bg="lightgray", show="*")

        self.txt_pass2.place(x=550, y=350, width=350, height=35)

        addUserButton = Button(addManagerFrame, text="Save Changings", cursor="hand2", bg="#097179", bd=4, fg="white",
                               font=("times new roman", 15, "bold"), command=self.function).place(x=500, y=510,
                                                                                                  width=200, height=50)

        # =============================== FLOOR FRAME =============================================

    def function(self):
        mb.showinfo("Successfully Changed", "User's value is changed successfully", parent=self.root)

    def logoutFunction(self):
        mb.askyesno("Logging out", "Are you sure you want to logout?", parent=self.root)
    # =============================== FLOOR FRAME =============================================

root = Tk()

obj = ChangeInformation(root)

root.mainloop()