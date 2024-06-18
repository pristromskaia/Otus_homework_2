"""Class Figure"""

from abc import ABC, abstractmethod

class Figure (ABC):
    """Class Figure"""

    @abstractmethod
    def get_area(self):
        """Find area"""

    @abstractmethod
    def get_perimeter(self):
        """Find perimeter"""

    def add_area(self, other_figure):
        """Check is figure and add area"""
        if not isinstance(other_figure, Figure):
            raise ValueError("Not a geometric figure")
        return self.get_area() + other_figure.get_area()

    def validate_side(self, side):
        """Validate side length"""
        if side <= 0:
            raise ValueError("Side length can not be less than 0")
