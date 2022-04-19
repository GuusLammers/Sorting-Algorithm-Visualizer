class Event:

    def __init__(self, payload=None) -> None:
        self.payload = payload


class ResetEvent(Event):

    def __init__(self) -> None:
        super().__init__()