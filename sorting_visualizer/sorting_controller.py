from tkinter.messagebox import NO
import sorting_model as sm  
import sorting_view as sv


class SortingController:

    def __init__(self, sorting_model: sm.SortingModel, sorting_view: sv.SortingView) -> None:
        self.sorting_model = sorting_model
        self.sorting_view = sorting_view

        self.update_sorting_view()

    def update_sorting_view(self) -> None:
        """Updates the sorting view to reflect changes in the sorting_model"""
        self.sorting_view.sorting_canvas.draw_sorting_bars(self.sorting_model.get_sorting_list())    