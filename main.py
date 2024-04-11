from tkinter import *


class DashBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Warehouse Management")
        self.root.config(bg="#c6e2ff")
        window_width = 1366
        window_height = 768
        self.root.geometry(f"{window_width}x{window_height}+"
                           f"{root.winfo_screenwidth() // 2 -
                              window_width // 2}+{root.winfo_screenheight() // 2 - window_height // 2}")
        self.root.resizable(False, False)


def wind():
    root = Tk()
    DashBoard(root)
    root.mainloop()


if __name__ == '__main__':
    wind()
