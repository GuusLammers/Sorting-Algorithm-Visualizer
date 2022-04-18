from main_model import *
from main_view import *

class MainController:

    def __init__(self, main_model: MainModel, main_view: MainView) -> None:
        self.main_view = main_view
        self.main_model = main_model