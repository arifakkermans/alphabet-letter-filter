"""Alphabet Filter"""
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


class LetterFilter(object):
    """
    Remove all the consonants or vowels from the given word.
    """

    vowels = ['a', 'e', 'i', 'o', 'u']

    def __init__(self, string: str):
        self.string = string

    def filter_vowels(self):
        """
        Removes all vowels from s and returns the string.

        Args:
            self: str representation

        Returns:
            string with all vowels
        """
        if not self.string.isascii():
            raise ValueError("It was not a ascii-encoded unicode string.")

        new_s = ''.join([x for x in self.string.lower() if x in LetterFilter.vowels])

        return new_s

    def filter_consonants(self):
        """
        Rmoves all consonants from s and returns the string.

        Args:
            self: str representation

        Returns:
            string with all vowels
        """
        if not self.string.isascii():
            raise ValueError("It was not a ascii-encoded unicode string.")

        new_s = ''.join(
            [x for x in self.string.lower() if x not in LetterFilter.vowels])

        return new_s

# input_string = str(input("Please enter a string: "))

# filter = LetterFilter(input_string)

# print (filter.filter_vowels())
# print (filter.filter_consonants())