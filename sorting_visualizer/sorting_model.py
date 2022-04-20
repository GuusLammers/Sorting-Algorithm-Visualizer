import random
import queue 
import time

import sorting_element as se
import color as c
import event as e
import sorting_algorithms as sa


class SortingModel:

    def __init__(self, list_size: int, event_queue: queue.Queue) -> None:
        self.list_size = list_size
        self.sorting_list: list[se.SortingElement] = list()
        self.event_queue = event_queue

        self.shuffle_sorting_list()

    def shuffle_sorting_list(self) -> None:
        """Creates a list of SortingElements that have a random value and the color Color.WHITE"""
        self.sorting_list = []
        for _ in range(self.list_size):
            rand = random.randint(1, self.list_size)
            self.sorting_list.append(se.SortingElement(rand, c.Color.WHITE))

    def get_sorting_list(self) -> "list[se.SortingElement]":
        return self.sorting_list       

    def send_update_event(self, sorting_list: "list[se.SortingElement]") -> None:
        """Creates an update event and adds it to the event queue"""
        update_event = e.UpdateEvent(sorting_list)
        self.event_queue.put_nowait(update_event)
        time.sleep(0.05)

    def set_index_white(self, index: int) -> None:
        """Sets element at index in sorting_list to the color white""" 
        self.sorting_list[index].set_color(c.Color.WHITE)

    def set_index_red(self, index: int) -> None:
        """Sets element at index in sorting_list to the color red""" 
        self.sorting_list[index].set_color(c.Color.RED) 

    def set_index_green(self, index: int) -> None:
        """Sets element at index in sorting_list to the color green""" 
        self.sorting_list[index].set_color(c.Color.GREEN) 

    def set_index_blue(self, index: int) -> None:
        """Sets element at index in sorting_list to the color blue""" 
        self.sorting_list[index].set_color(c.Color.BLUE)           

    def sort(self, sorting_algorithm: str) -> None:
        """Runs passed in sorting algorithm"""
        if sorting_algorithm == "selection sort":
            sa.selection_sort(
                sorting_list=self.sorting_list, 
                event_queue=self.event_queue)
        elif sorting_algorithm == "quick sort":
            sa.quick_sort(
                sorting_list=self.sorting_list.copy(), 
                low=0, 
                high=len(self.sorting_list) - 1, 
                event_queue=self.event_queue, 
                level=0)     
        elif sorting_algorithm == "merge sort":
            sa.merge_sort(
                sorting_list=self.sorting_list, 
                left=0, 
                right=len(self.sorting_list) - 1, 
                event_queue=self.event_queue,
                level=0)    
        elif sorting_algorithm == "insertion sort":
            sa.insertion_sort(
                sorting_list=self.sorting_list,
                event_queue=self.event_queue
            ) 
        elif sorting_algorithm == "cocktail sort":
            sa.cocktail_sort(
                sorting_list=self.sorting_list,
                event_queue=self.event_queue
            )            
