import queue
import time

import sorting_element as se
import color as c
import event as e



def update(sorting_list: "list[se.SortingElement]", event_queue: queue.Queue) -> None:
    """Sends an update event into the event queue"""
    event_queue.put_nowait(e.UpdateEvent(sorting_list))
    time.sleep(0.05)

def sort_complete(sorting_list: "list[se.SortingElement]", event_queue: queue.Queue) -> None:
    """Turns all sorting elements green and sends the required update evenets into the event queue"""
    for element in sorting_list:
        element.set_color(c.Color.GREEN)
        update(sorting_list, event_queue)


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



def quick_sort(sorting_list: "list[se.SortingElement]", low: int, high: int, event_queue: queue.Queue, level: int) -> None:
    """Quick sort altered to update colors of sorting elements at specific times"""
    if low < high:
        # Find pivot element such that element smaller than pivot are on the left element greater than pivot are on the right
        # pivot is in its correct position after partition is called
        pi = quick_sort_partition(sorting_list, low, high, event_queue)
        sorting_list[pi].set_color(c.Color.GREEN)
    
        # Recursive call on the left side of pivot
        quick_sort(sorting_list, low, pi - 1, event_queue, level + 1)
    
        # Recursive call on the right side of pivot
        quick_sort(sorting_list, pi + 1, high, event_queue, level + 1)

        # if the recursion returns back to the top of the recursive stack the sort is complete
        if level == 0:
            sort_complete(sorting_list, event_queue)


def quick_sort_partition(sorting_list: "list[se.SortingElement]", low: int, high: int, event_queue: queue.Queue) -> int:
    """Partition function that is used by quick sort. The element at index high is chosen as the pivot"""
    # choose the rightmost element as pivot
    pivot = sorting_list[high]
    
    # pointer for greater element
    i = low - 1
    
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if sorting_list[j].get_value() <= pivot.get_value():
        # if element smaller than pivot is found swap it with the greater element pointed by i
            i = i + 1
            # swapping element at i with element at j
            sorting_list[i], sorting_list[j] = sorting_list[j], sorting_list[i]
            update(sorting_list, event_queue)
        
    # swap the pivot element with the greater element specified by i
    sorting_list[i + 1], sorting_list[high] = sorting_list[high], sorting_list[i + 1]
    update(sorting_list, event_queue)
    
    # return the position from where partition is done
    return i + 1



def merge_sort(sorting_list: "list[se.SortingElement]", left: int, right: int, event_queue: queue.Queue, level: int) -> None:
    """Merge sort altered to update colors of sorting elements at specific times"""
    if (left < right):
        middle = left + (right - left) // 2
        # Sort and merge first and second halves
        merge_sort(sorting_list, left, middle, event_queue, level + 1)
        merge_sort(sorting_list, middle + 1, right, event_queue, level + 1)
        merge_sort_merge(sorting_list, left, middle, right, event_queue)

        # if the recursion returns back to the top of the recursive stack the sort is complete
        if level == 0:
            sort_complete(sorting_list, event_queue)


def merge_sort_merge(sorting_list: "list[se.SortingElement]", start: int, mid: int, end: int, event_queue: queue.Queue) -> None:
    """Merge function used by merge sort"""
    start2 = mid + 1
    # if the direct merge is already sorted
    if (sorting_list[mid].get_value() <= sorting_list[start2].get_value()):
        return
 
    # two pointers to maintain start of both lists to merge
    while (start <= mid and start2 <= end):
        # if element 1 is in right place
        if (sorting_list[start].get_value() <= sorting_list[start2].get_value()):
            start += 1
        else:
            value = sorting_list[start2]
            index = start2
            # shift all the elements between element 1 element 2, right by 1.
            while (index != start):
                sorting_list[index] = sorting_list[index - 1]
                sorting_list[index].set_color(c.Color.RED)
                update(sorting_list, event_queue)
                sorting_list[index].set_color(c.Color.WHITE)
                index -= 1
 
            sorting_list[start] = value
            # update all the pointers
            start += 1
            mid += 1
            start2 += 1



def insertion_sort(sorting_list: "list[se.SortingElement]", event_queue: queue.Queue) -> None:
    """Insertion sort altered to update colors of sorting elements at specific times"""
    # traverse through 1 to len(arr)
    for i in range(1, len(sorting_list)):
        key = sorting_list[i]
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i-1
        while j >= 0 and key.get_value() < sorting_list[j].get_value():
                sorting_list[j + 1] = sorting_list[j]
                sorting_list[j + 1].set_color(c.Color.RED)
                update(sorting_list, event_queue)
                sorting_list[j + 1].set_color(c.Color.WHITE)
                j -= 1

        # insert key back into the list at its correct location
        sorting_list[j + 1] = key
        sorting_list[j + 1].set_color(c.Color.BLUE)
        update(sorting_list, event_queue)
        sorting_list[j + 1].set_color(c.Color.WHITE)

    # sort completed
    sort_complete(sorting_list, event_queue) 



def cocktail_sort(sorting_list: "list[se.SortingElement]", event_queue: queue.Queue) -> None:
    """Cocktail sort altered to update colors of sorting elements at specific times"""
    n = len(sorting_list)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
        # reset the swapped flag on entering the loop, because it might be true from a previous iteration.
        swapped = False
        # loop from left to right moving the largest element found
        for i in range (start, end):
            sorting_list[i].set_color(c.Color.BLUE)
            update(sorting_list, event_queue)
            sorting_list[i].set_color(c.Color.WHITE)
            if (sorting_list[i].get_value() > sorting_list[i+1].get_value()) :
                sorting_list[i], sorting_list[i+1]= sorting_list[i+1], sorting_list[i]
                swapped=True
  
        sorting_list[end].set_color(c.Color.GREEN)
        # if nothing moved, then array is sorted.
        if (swapped==False):
            break
  
        # reset the swapped flag so that it can be used in the next stage
        swapped = False
        # move the end point back by one, because item at the end is in its rightful spot
        end = end-1
        # loop from right to left
        for i in range(end-1, start-1,-1):
            sorting_list[i+1].set_color(c.Color.BLUE)
            update(sorting_list, event_queue)
            sorting_list[i+1].set_color(c.Color.WHITE)
            if (sorting_list[i].get_value() > sorting_list[i+1].get_value()):
                sorting_list[i], sorting_list[i+1] = sorting_list[i+1], sorting_list[i]
                swapped = True
  
        sorting_list[start].set_color(c.Color.GREEN)
        # increase the starting point, because the last stage would have moved the next smallest number to its rightful spot.
        start = start+1       

    # sort complete  
    sort_complete(sorting_list, event_queue)  