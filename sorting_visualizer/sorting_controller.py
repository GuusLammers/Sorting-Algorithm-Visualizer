import queue
import time
import threading

import sorting_model as sm  
import sorting_view as sv
import event as e


class SortingController:

    def __init__(self, sorting_model: sm.SortingModel, sorting_view: sv.SortingView, event_queue: queue.Queue) -> None:
        self.sorting_model = sorting_model
        self.sorting_view = sorting_view
        self.event_queue = event_queue

        self.update_sorting_view()

    def update_sorting_view(self) -> None:
        """Updates the sorting view to reflect changes in the sorting_model"""
        self.sorting_view.reload_sorting_canvas(self.sorting_model.get_sorting_list())  

    def start_event_listener(self) -> None:
        """Listens for events posted to the event_queue"""    
        while True:
            # if queue is not empty
            if not self.event_queue.empty():
                event = self.event_queue.get_nowait()
                if isinstance(event, e.ResetEvent):
                    """Resets sorting list"""
                    self.sorting_model.shuffle_sorting_list()
                    self.update_sorting_view()
                elif isinstance(event, e.StartEvent):
                    print(event.payload)    
            # if queue is empty
            else:        
                time.sleep(0.1)