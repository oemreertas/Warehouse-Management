import tkinter as tk


def create_button(self, text, command, x, y):
    button = tk.Button(self, text=text, command=command)
    button.configure(bg="#1c6071", fg="white", font=("Arial", 15, "bold"),
                     takefocus=False, bd=0, cursor="hand2", activebackground="#1c6071",
                     activeforeground="gray")
    button.place(x=x, y=y)
    return button


class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Warehouse Management")
        self.geometry("1366x768+{}+{}".format(self.winfo_screenwidth() // 2 - 1366 // 2,
                                              self.winfo_screenheight() // 2 - 768 // 2))
        self.resizable(False, False)
        self.config(bg="#fffafa")

        self.create_sidebar()

    def create_sidebar(self):
        sidebar_frame = tk.Frame(self, bg="#1c6071", width=240, height=768)
        sidebar_frame.pack(side="left")

        create_button(sidebar_frame, "Dashboard", self.do_nothing, x=50, y=50)
        create_button(sidebar_frame, "Orders", self.do_nothing, x=50, y=100)

    def do_nothing(self):
        pass


if __name__ == '__main__':
    app = Dashboard()
    app.mainloop()
