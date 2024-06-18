"""Square class"""

from src.rectangle import Rectangle

class Square(Rectangle):
    """Square class"""
    def __init__(self, side_a):
        self.validate_side(side_a)
        super().__init__(side_a, side_a)
