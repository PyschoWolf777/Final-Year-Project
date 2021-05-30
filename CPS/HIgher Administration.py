from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as mb

class HigherAdministration:
    def __init__(self, root):
        self.root=root
        self.root.title("Higher Admin Panel")
        self.root.geometry("1199x600+0+50")

        self.root.resizable(False, False)
        #=========== Setting  Frames ================

        mainFrame = Frame(self.root, bg = "white").place(width = 1199, height = 600)

        upperFrame = Frame(mainFrame, bg="#097179").place(x=0, y=0, width=1199, height=100)

        sideFrame = Frame(mainFrame, bg="#097179").place(x=0, y=100, width=200, height=500)

        bodyFrame = Frame(mainFrame, bg="#097179").place(x=200, y=100, width=999, height=500)


        #=============================================================================================
        #--------------------------- UPPER FRAME -----------------------------------------------------
        #=============================================================================================
        #================ Add image logo image to the upper frame

        self.photo = PhotoImage(file='logo.png')  # this command will get the photo from your project, for showing it on GUI, first add this into label
        self.lbl = Label(upperFrame, image=self.photo)
        self.lbl.place(x=10, y=10, width=150, height = 80)

        #================== TITLE
        title = Label(upperFrame, text="CORONA PREVENTION SYSTEM", font=("Impact", 35, "bold"), fg="white", bg="#097179").place(
            x=200, y=20)

        #=============== WELCOME The USER

        welcomeLabel = Label(upperFrame, text="Welcome!", font=("Impact", 20, "bold"), fg="white", bg="#097179").place(x=950, y =15)
        userNameLabel = Label(upperFrame, text="Hamza", font=("Impact", 15), fg="white", bg="#097179").place(
            x=950, y=55)
        #================= Drop Down Arrow button
        self.downButtonPhoto = PhotoImage(file = "logout.png", width = 40, height = 40)
        self.downButton = Label(upperFrame, image=self.downButtonPhoto)
        #self.downButton.place(x=1000, y=10, width= 50, height=50)

        #HERE COMMAND IS TO BE ADDED
        #dropButton = Button(upperFrame, image = self.downButtonPhoto, cursor = "hand2", bg = "red").place(x=1130, y=30, width= 40, height=40)
        dropButton = Button(upperFrame, text="Logout", cursor="hand2", fg = "white",
                            bg="#097179", font = ("Times new roman", 12, "bold"), bd = 3, relief = SUNKEN
                            , command= self.function).place(x=1100, y=30,
                                                                                                    width=70, height=50)

        #=============================================================================================
        #--------------------------- SIDE FRAME -----------------------------------------------------
        #=============================================================================================

        floorButton = Button(sideFrame, text="Floors", cursor="hand2", bg="#097179", bd=0, fg="white",
                              font=("times new roman", 20, "bold")).place(x = 0, y = 100,width= 200, height = 100)

        violationButton = Button(sideFrame, text="Violations", cursor="hand2", bg="#097179", bd=0, fg="white",
                              font=("times new roman", 20,"bold")).place(x=0, y=200, width=200, height=100)

        settingButton = Button(sideFrame, text="Setting", cursor="hand2", bg="#097179", bd=0, fg="white",
                              font=("times new roman", 20, "bold")).place(x=0, y=300, width=200, height=100)

        recordButton = Button(sideFrame, text="Record", cursor="hand2", bg="#097179", bd=0, fg="white",
                              font=("times new roman", 20, "bold")).place(x=0, y=400, width=200, height=100)

        changeUserButton = Button(sideFrame, text="User", cursor="hand2", bg="#097179", bd=0, fg="white",
                              font=("times new roman", 20, "bold")).place(x=0, y=500, width=200, height=100)
        '''
        for frame in ():
            frame.grid(row=0, column=0)
        '''
        # =============================================================================================
        # --------------------------- Body FRAME -----------------------------------------------------
        # =============================================================================================


        #=============================== FLOOR FRAME =============================================

        floorFrame = Frame(bodyFrame, bg = "#04c0cf").place(x = 200, y = 100,width= 999, height = 500);

        settingButton = Button(floorFrame, text="Ground Floor", cursor="hand2", bg="#097179", fg="white",
                               font=("times new roman", 20, "bold")).place(x= 250, y=150, width= 400, height=100)

        settingButton = Button(floorFrame, text="First Floor", cursor="hand2", bg="#097179", fg="white",
                               font=("times new roman", 20, "bold")).place(x= 750, y=150, width= 400, height=100)

        settingButton = Button(floorFrame, text="Second Floor", cursor="hand2", bg="#097179", fg="white",
                               font=("times new roman", 20, "bold")).place(x= 250, y=350, width= 400, height=100)

        settingButton = Button(floorFrame, text="Third Floor", cursor="hand2", bg="#097179", fg="white",
                               font=("times new roman", 20, "bold")).place(x= 750, y=350, width= 400, height=100)


    def function(self):
        mb.askyesno("Confirmation", "Are you sure you want to logout?")
        # =============================== FLOOR FRAME =============================================



root = Tk()

obj = HigherAdministration(root)

root.mainloop()