import queue 
import threading

import sorting_model as sm  
import sorting_view as sv
import sorting_controller as sc


if __name__ == "__main__":
    # thread safe queue
    event_queue = queue.Queue()

    sorting_model = sm.SortingModel(100, event_queue)
    sorting_view = sv.SortingView(event_queue)
    sorting_controller = sc.SortingController(sorting_model, sorting_view, event_queue)

    # start event listener on a daemon thread
    threading.Thread(target=sorting_controller.start_event_listener, daemon=True).start()

    # start tkinter mainloop 
    sorting_view.mainloop()