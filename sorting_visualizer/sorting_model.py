import random
import queue 

import sorting_element as se
import color as c


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

