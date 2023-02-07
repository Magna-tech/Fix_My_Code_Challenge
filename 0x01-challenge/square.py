#!/usr/bin/python3
"""Class square"""


class square:
    """Class square"""

    def __init__(self, width = 0):
        """Initialization"""
        self.__width = width

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Perimeter"""
        return (self.width * 4)

    def __str__(self):
        """Print sides"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    s = square(12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
