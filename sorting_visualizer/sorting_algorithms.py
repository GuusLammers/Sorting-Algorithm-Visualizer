import queue
import time

import sorting_element as se
import color as c
import event as e



def update(sorting_list: "list[se.SortingElement]", event_queue: queue.Queue) -> None:
    event_queue.put_nowait(e.UpdateEvent(sorting_list))
    time.sleep(0.05)


def selection_sort(sorting_list: "list[se.SortingElement]", event_queue: queue.Queue) -> None:    
        """Selection sort altered to update colors of sorting elements at specific times"""
        # traverse through all the elements in sorting_list
        for i in range(len(sorting_list)):
            # find minimum element in remaining unsorted list
            minimum_index = i
            sorting_list[minimum_index].set_color(c.Color.RED)
            for j in range(minimum_index + 1, len(sorting_list)):
                sorting_list[j].set_color(c.Color.BLUE)
                update(sorting_list, event_queue)
                sorting_list[j].set_color(c.Color.WHITE) 
                if sorting_list[minimum_index].get_value() > sorting_list[j].get_value():
                    sorting_list[minimum_index].set_color(c.Color.WHITE)
                    minimum_index = j
                    sorting_list[minimum_index].set_color(c.Color.RED)

            # swap elements  
            sorting_list[i], sorting_list[minimum_index] = sorting_list[minimum_index], sorting_list[i] 
            sorting_list[i].set_color(c.Color.GREEN)
            update(sorting_list, event_queue)

    
def quick_sort(sorting_list: "list[se.SortingElement]", low: int, high: int, event_queue: queue.Queue) -> None:
    """Quick sort altered to update colors of sorting elements at specific times"""
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = quick_sort_partition(sorting_list, low, high, event_queue)
        sorting_list[pi].set_color(c.Color.GREEN)
    
        # Recursive call on the left of pivot
        quick_sort(sorting_list, low, pi - 1, event_queue)
    
        # Recursive call on the right of pivot
        quick_sort(sorting_list, pi + 1, high, event_queue)


def quick_sort_partition(sorting_list: "list[se.SortingElement]", low: int, high: int, event_queue: queue.Queue) -> int:
    """Partition function that is used by quick sort"""
    # Choose the rightmost element as pivot
    pivot = sorting_list[high]
    
    # Pointer for greater element
    i = low - 1
    
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if sorting_list[j].get_value() <= pivot.get_value():
        # If element smaller than pivot is found
        # swap it with the greater element pointed by i
            i = i + 1
        
            # Swapping element at i with element at j
            sorting_list[i], sorting_list[j] = sorting_list[j], sorting_list[i]
            update(sorting_list, event_queue)
        
    # Swap the pivot element with the greater element specified by i
    sorting_list[i + 1], sorting_list[high] = sorting_list[high], sorting_list[i + 1]
    update(sorting_list, event_queue)
    
    # Return the position from where partition is done
    return i + 1