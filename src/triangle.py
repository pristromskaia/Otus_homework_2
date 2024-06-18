"""Triangle class"""

import math
from src.figure import Figure

class Triangle(Figure):
    """Triangle class"""

    def __init__(self, side_a, side_b, side_c):
        self.validate_side(side_a)
        self.validate_side(side_b)
        self.validate_side(side_c)
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("Triangle with such sides length does not exist")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        s = self.get_perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
