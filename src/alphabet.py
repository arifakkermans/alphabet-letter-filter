"""Alphabet Filter"""
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


class LetterFilter:
    """
    Remove all the consonants or vowels from the given word.
    """

    vowels = ['a', 'e', 'i', 'o', 'u']

    def init(self, string: str):
        self.string = string

    def filter_vowels(self,  string: str):
        """
        Removes all vowels from s and returns the string.

        Args:
            self: str representation

        Returns:
            string with all vowels
        """
        if not string.isascii():
            raise ValueError("It was not a ascii-encoded unicode string.")

        new_s = ''.join([x for x in string.lower() if x in LetterFilter.vowels])

        return new_s

    def filter_consonants(self, string: str):
        """
        Rmoves all consonants from s and returns the string.

        Args:
            self: str representation

        Returns:
            string with all vowels
        """
        if not string.isascii():
            raise ValueError("It was not a ascii-encoded unicode string.")

        new_s = ''.join(
            [x for x in string.lower() if x not in LetterFilter.vowels])

        return new_s

# input_string = str(input("Please enter a string: "))

# filter = LetterFilter()

# print (filter.filter_vowels(input_string))
# print (filter.filter_consonants(input_string))