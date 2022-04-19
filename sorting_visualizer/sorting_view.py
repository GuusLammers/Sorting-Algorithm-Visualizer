import tkinter as tk

import sorting_element as se


class SortingView(tk.Tk):

    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.main_frame = tk.Frame(self)
        self.resizable(width=False, height=False)

        self.navigation_bar_frame = NavigationBarFrame(self)
        self.sorting_canvas = SortingCanvas(self)

        self.navigation_bar_frame.grid(row=0, column=0)
        self.sorting_canvas.grid(row=1, column=0)



class NavigationBarFrame(tk.Frame):

    def __init__(self, parent) -> None:
        tk.Frame.__init__(self, parent)

        self.configure(height=50, width=1000)

        self.configure(background="black", highlightbackground="grey", highlightthickness=2)



class SortingCanvas(tk.Canvas):

    def __init__(self, parent) -> None:
        tk.Canvas.__init__(self, parent)
        self.width = 1000
        self.height = 750
        self.configure(width=self.width, height=self.height, border=0, highlightthickness=0)
        self.configure(background="black")


    def draw_sorting_bars(self, sorting_list: se.SortingElement):
        """Clears the canvas and then redraws the sorting bars onto the canvas"""
        # clear canvas
        self.delete("all")

        # redraw sorting bars
        bar_width = 10
        gap = 1
        print("Bar Width: ", bar_width)
        for i, sorting_element in enumerate(sorting_list):
            height = int((sorting_element.get_value() / len(sorting_list)) * self.height)
            x0 = i * bar_width + gap
            y0 = 0
            x1 = x0 + bar_width - gap
            y1 = height
            self.create_rectangle(x0, y0, x1, y1, width=0, fill="white")


