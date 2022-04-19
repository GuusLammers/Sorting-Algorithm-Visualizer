import tkinter as tk
import queue

import sorting_element as se
import event as e


class SortingView(tk.Tk):

    def __init__(self, event_queue: queue.Queue) -> None:
        tk.Tk.__init__(self)
        self.main_frame = tk.Frame(self)
        self.resizable(width=False, height=False)

        self.event_queue = event_queue

        self.navigation_bar_frame = NavigationBarFrame(self, self.event_queue)
        self.sorting_canvas = SortingCanvas(self)

        self.navigation_bar_frame.grid(row=0, column=0)
        self.sorting_canvas.grid(row=1, column=0)

    def reload_sorting_canvas(self,  sorting_list: se.SortingElement):
        """Reloads canvas by destroying current canvas and replacing it with a new one"""
        new_sorting_canvas = SortingCanvas(self)
        new_sorting_canvas.draw_sorting_bars(sorting_list)
        new_sorting_canvas.grid(row=1, column=0)
        
        self.sorting_canvas.destroy()
        self.sorting_canvas = new_sorting_canvas


class NavigationBarFrame(tk.Frame):

    def __init__(self, parent, event_queue: queue.Queue) -> None:
        self.event_queue = event_queue
        
        tk.Frame.__init__(self, parent)
        self.configure(height=50, width=1000)
        self.configure(background="black", highlightbackground="grey", highlightthickness=2)


        self.reset_button = tk.Button(self, text="Reset", command=self.send_reset_event)
        self.reset_button.grid(row=0, column=0)

        self.start_button = tk.Button(self, text="Start", command=self.send_start_event)
        self.start_button.grid(row=0, column=1)

        self.drop_down_menu_value = tk.StringVar(self)
        self.choices = [
            "insertion sort",
            "merge sort"
        ]
        self.drop_down_menu_value.set(self.choices[0])
        self.drop_down_menu = tk.OptionMenu(self, self.drop_down_menu_value, *self.choices)
        self.drop_down_menu.grid(row=0, column=2)

    def send_reset_event(self) -> None:
        """Adds a reset event to the event queue"""
        reset_event = e.ResetEvent()
        self.event_queue.put_nowait(reset_event)

    def send_start_event(self) -> None:
        """Adds a start event to the event queue"""
        start_event = e.StartEvent(self.drop_down_menu_value.get())
        self.event_queue.put_nowait(start_event)    


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
        for i, sorting_element in enumerate(sorting_list):
            height = int((sorting_element.get_value() / len(sorting_list)) * self.height)
            x0 = i * bar_width + gap
            y0 = 0
            x1 = x0 + bar_width - gap
            y1 = height
            self.create_rectangle(x0, y0, x1, y1, width=0, fill="white")


