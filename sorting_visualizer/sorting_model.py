import random
import queue 
import time

import sorting_element as se
import color as c
import event as e


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

    def send_update_event(self) -> None:
        """Creates an update event and adds it to the event queue"""
        update_event = e.UpdateEvent()
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

    def selection_sort(self) -> None:    
        # traverse through all the elements in sorting_list
        for i in range(len(self.sorting_list)):
            # find minimum element in remaining unsorted list
            minimum_index = i
            self.set_index_red(minimum_index)
            for j in range(minimum_index + 1, len(self.sorting_list)):
                self.set_index_blue(j)
                self.send_update_event()
                self.set_index_white(j) 
                if self.sorting_list[minimum_index].get_value() > self.sorting_list[j].get_value():
                    self.set_index_white(minimum_index)
                    minimum_index = j
                    self.set_index_red(minimum_index)

            # swap elements  
            self.sorting_list[i], self.sorting_list[minimum_index] = self.sorting_list[minimum_index], self.sorting_list[i] 
            self.set_index_green(i)
            self.send_update_event()    