from tkinter import *
import HIgher_Administration

class SupportFunctions:
    def __init__(self, root):
        self.root = root

    def floors(self):
        aa = HIgher_Administration.HigherAdministration(self.root)

if __name__ == '__main__':
    root = Tk()

    obj = SupportFunctions(root)

    root.mainloop()