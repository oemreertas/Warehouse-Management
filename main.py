from tkinter import *


class MenuButton(Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(font=("Arial", 30, "Bold"))


root = Tk()
root.title("Warehouse Management")
root.config(bg="#c6e2ff")
window_width = 1300
window_height = 800
root.geometry(f"{window_width}x{window_height}+"
              f"{root.winfo_screenwidth() // 2 -
                 window_width // 2}+{root.winfo_screenheight() // 2 - window_height // 2}")
root.resizable(False, False)

button_frame = Frame(root)
button_frame.config(width=300, height=800, bg="red")
button_frame.pack(side="left")


root.mainloop()
