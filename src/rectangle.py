"""Rectangle class"""

from src.figure import Figure

class Rectangle(Figure):
    """Rectangle class"""

    def __init__(self, side_a, side_b):
        self.validate_side(side_a)
        self.validate_side(side_b)
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_b * self.side_a

    def get_perimeter(self):
        return 2 * (self.side_b + self.side_a)
