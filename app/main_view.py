import tkinter as tk

class MainView(tk.Tk):

    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.main_frame = tk.Frame(self)

    def setup_main_frame(self) -> None:
        self.main_frame.height = 1000
        self.main_frame.width = 1000
        self.main_frame.pack()
