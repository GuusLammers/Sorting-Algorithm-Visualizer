from main_model import *
from main_view import *
from main_controller import *

if __name__ == "__main__":
    main_model = MainModel()
    main_view = MainView()
    main_controller = MainController(main_model, main_view)
