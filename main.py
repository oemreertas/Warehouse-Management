from tkinter import *
from tkinter import ttk


class DashBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Warehouse Management")
        self.root.config(bg="#fffafa")
        window_width = 1366
        window_height = 768
        self.root.geometry(f"{window_width}x{window_height}+"
                           f"{root.winfo_screenwidth() // 2 -
                              window_width // 2}+{root.winfo_screenheight() // 2 - window_height // 2}")
        self.root.resizable(False, False)
        '''====================SIDE BAR=============================='''
        'Frame Options'

        self.SideFrame = ttk.Frame(root, style="Custom.TFrame", width=268, height=768)
        self.SideFrame.pack(side="left", fill="y", expand=False)

        self.style = ttk.Style()
        self.style.theme_use('alt')

        "Buttons Style"
        self.style.configure("Custom.TButton", foreground="white", font=("Helvetica", 12, "bold"),
                             background='#2f4f4f', borderwidth=0)
        self.style.map('Custom.TButton',
                       background=[('active', '#2f4f4f'), ('disabled', '#f0f0f0')])

        "Side Bar Frame Style"
        self.style.configure("Custom.TFrame", background="#2f4f4f")

        self.button1 = ttk.Button(self.SideFrame, text="BUTTON1", style="Custom.TButton", takefocus=False,
                                  width=28, padding=4)
        self.button1.place(x=0, y=170)


def wind():
    root = Tk()
    DashBoard(root)
    root.mainloop()


if __name__ == '__main__':
    wind()
