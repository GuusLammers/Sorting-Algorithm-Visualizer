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
        if sorting_algorithm == "insertion sort":
            sa.selection_sort(self.sorting_list, self.event_queue)
        elif sorting_algorithm == "quick sort":
            print("Length: ", len(self.sorting_list))
            sa.quick_sort(self.sorting_list.copy(), 0, len(self.sorting_list) - 1, self.event_queue)     






   


    def quick_sort(self, arr, low, high) -> None:
        """Quick sort altered to update colors of sorting elements at specific times"""
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = self.quick_sort_partition(arr, low, high)
        
            # Recursive call on the left of pivot
            self.quick_sort(arr, low, pi - 1)
        
            # Recursive call on the right of pivot
            self.quick_sort(arr, pi + 1, high)

    def quick_sort_partition(self, arr, low, high) -> int:
        """Partition function that is used by quick sort"""
        # Choose the rightmost element as pivot
        pivot = self.sorting_list[high]
        
        # Pointer for greater element
        i = low - 1
        
        # Traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if self.sorting_list[j].get_value() <= pivot.get_value():
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
                i = i + 1
            
                # Swapping element at i with element at j
                (self.sorting_list[i], self.sorting_list[j]) = (self.sorting_list[j], self.sorting_list[i])
                self.send_update_event(arr)
            
            # Swap the pivot element with the greater element specified by i
            (self.sorting_list[i + 1], self.sorting_list[high]) = (self.sorting_list[high], self.sorting_list[i + 1])
            self.send_update_event(arr)
            
            # Return the position from where partition is done
            return i + 1