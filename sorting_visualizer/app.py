import sorting_model as sm  
import sorting_view as sv
import sorting_controller as sc


if __name__ == "__main__":
    sorting_model = sm.SortingModel(100)
    sorting_view = sv.SortingView()
    sorting_controller = sc.SortingController(sorting_model, sorting_view)

    sorting_view.mainloop()