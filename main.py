import tkinter as tk
from tkinter.font import Font


def create_button(parent, text, command, x, y, img=None):
    button = tk.Button(parent, text=text, command=command, image=img, compound="left")
    button.configure(bg="#1c6071", fg="Silver", font=("Arial", 13, "bold"),
                     takefocus=False, bd=0, cursor="hand2", activebackground="#1c6071",
                     activeforeground="gray")

    button.place(x=x, y=y)
    button.bind("<Enter>",
                lambda event: button.after(170, lambda: button.configure(bg="#1c6071", font=("Arial", 13, "bold"),
                                                                         foreground="gray")))
    button.bind("<Leave>",
                lambda event: button.after(170, lambda: button.configure(bg="#1c6071", fg="Silver", font=("Arial", 13, "bold"),
                                                                         takefocus=False, bd=0, cursor="hand2",
                                                                         activebackground="#1c6071")))
    return button


def create_label(parent, x, y, text, foreground):
    label = tk.Label(parent, text=text, foreground=foreground)
    label.configure(background="#1c6071", font=("Roboto", 14))
    label.place(x=x, y=y)
    return label




class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Warehouse Management")
        self.geometry("1366x768+{}+{}".format(self.winfo_screenwidth() // 2 - 1366 // 2,
                                              self.winfo_screenheight() // 2 - 768 // 2))
        self.resizable(False, False)
        self.config(bg="#fffafa")
        self.images = {
            "dashboard": tk.PhotoImage(file="images/dashboard.png").subsample(4, 4),
            "main": tk.PhotoImage(file="images/mainimage.png"),
            "inventory": tk.PhotoImage(file="images/inventory.png").subsample(3, 3),
            "purchaseorders": tk.PhotoImage(file="images/purchoseorders.png").subsample(3, 3),
            "salesorders": tk.PhotoImage(file="images/salesorders.png").subsample(4, 4),
            "customers": tk.PhotoImage(file="images/costumers.png").subsample(4, 4),
            "reports": tk.PhotoImage(file="images/reports.png").subsample(4, 4),
            "options": tk.PhotoImage(file="images/options.png")

        }
        self.fonts = {
            "Roboto": Font(family="fonts/Roboto/Roboto-Thin.ttf", size=15),

        }

        self.Sidebar()
        self.Dashboard()


    def Sidebar(self):
        sidebar_frame = tk.Frame(self, bg="#1c6071", width=240, height=768)
        sidebar_frame.pack(side="left")

        create_button(sidebar_frame, " Dashboard", self.do_nothing, x=30, y=150, img=self.images["dashboard"])
        create_button(sidebar_frame, " Inventory", self.do_nothing, x=30, y=210, img=self.images["inventory"])
        create_button(sidebar_frame, " Purchase Orders", self.do_nothing, x=30, y=270,
                      img=self.images["purchaseorders"])
        create_button(sidebar_frame, " Sales Orders", self.do_nothing, x=30, y=330,
                      img=self.images["salesorders"])
        create_button(sidebar_frame, " Customers", self.do_nothing, x=30, y=390,
                      img=self.images["customers"])
        create_button(sidebar_frame, " Reports", self.do_nothing, x=30, y=450,
                      img=self.images["reports"])
        create_button(sidebar_frame, " Options", self.do_nothing, x=30, y=700,
                      img=self.images["options"])
        create_button(sidebar_frame, img=self.images["main"], x=5, y=5, text="", command="").configure(cursor="",
                                                                                                       takefocus=False)
        create_label(sidebar_frame, x=100, y=13, text="WareHouse\nManagement", foreground="pink")
        create_label(sidebar_frame, x=100 , y=60, text="Version 1.00", foreground="silver").configure(font=("arial", 8))

    def Dashboard(self):
        dashboard_frame = tk.Frame(self, background="#fffafa", width=1126, height=768)
        dashboard_frame.pack(side="right")

        label1 = tk.Label(dashboard_frame, width=10, height=5, background="red", borderwidth=4).place(x= 150, y= 150)

    def do_nothing(self):
        pass

if __name__ == '__main__':
    app = Main()
    app.mainloop()
