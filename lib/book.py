#!/usr/bin/env python3

class Book:
    """A class representing a book with a title and page count."""
    
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        """Simulates turning a page in the book."""
        print("Flipping the page...wow, you read fast!")

    @property
    def page_count(self):
        """Gets the page count of the book."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        self._page_count = value

    @property
    def title(self):
        """Gets the title of the book."""
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("title must be a string")
        self._title = value

    def __str__(self):
        return f"{self.title} has {self.page_count} pages"
