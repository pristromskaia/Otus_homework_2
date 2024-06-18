"""Circle class"""

import math
from src.figure import Figure

class Circle(Figure):
    """Circle class"""

    def __init__(self, radius):
        self.validate_side(radius)
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.radius
