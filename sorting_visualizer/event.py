class Event:
    pass


class ResetEvent(Event):

    def __init__(self) -> None:
        super().__init__()

class StartEvent(Event):

    def __init__(self, payload) -> None:
        self.payload = payload  

class UpdateEvent(Event):

    def __init__(self, payload) -> None:
        self.payload = payload              