#!/usr/bin/env python3

class CountedIterator:
    """
    Iterator class that counts the number of iterations.
    It works by wrapping any iterable and keeping track of how many times
    the next() method has been called.
    """

    def __init__(self, iterable):
        """
        Initialize the iterator with the given iterable.

        :param iterable: The iterable to be wrapped.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator object itself.
        This is required for Python's iterator protocol.
        """
        return self

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.

        If the iterator is exhausted, raise StopIteration.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration  # Just to be explicit, but this is redundant.

    def get_count(self):
        """
        Return the number of iterations so far.

        :return: The count of next() calls.
        """
        return self.count
