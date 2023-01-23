import unittest

from main import capitalize


class CapitalizeTests(unittest.TestCase):

    def test_capitalized_phrase(self):
        # given a phrase and its capitalization
        for (desc, phrase, expected) in (
                ("empty string", "", ""),
                ("single character", "a", "A"),
                ("single ASCII word", "hello", "Hello"),
                ("single Unicode word", "èlo", "Èlo"),
                ("already capitalized word", "Hello", "Hello"),
                ("ASCII phrase", "hello world!", "Hello World!"),
                ("Unicode phrase", "world èlo", "World Èlo"),
        ):
            with self.subTest(desc):
                # when the phrase is capitalized
                capitalized = capitalize(phrase)

                # then it is capitalized as expected
                self.assertEqual(capitalized, expected)
