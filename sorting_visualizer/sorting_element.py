import color as c


class SortingElement:

    def __init__(self, value: int, color: c.Color) -> None:
        self._value = value
        self.color = color

    def get_value(self) -> int:
        return self._value

    def get_color(self) -> str:  
        """Returns value of Enum"""
        return self.color.value

    def set_color(self, color: c.Color) -> None:      
        self.color = color
