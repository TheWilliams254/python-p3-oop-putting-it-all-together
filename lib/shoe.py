#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition="New"):
        self._condition = condition
        self.brand = brand
        self.size = size
    pass

    @property
    def condition(self):
        return self._condition

    @property
    def brand(self):
        """Gets the brand of the shoe."""
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise TypeError("brand must be a string")
        self._brand = value

    @property
    def size(self):
        """Gets the size of the shoe."""
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        pass
    

