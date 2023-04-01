from src.main import Main
from unittest import TestCase


class MainTest(TestCase):
    def test_say_hello(self):
        expect = "Hello World, Fulano!"
        actual = Main().say_hello("Fulano")
        self.assertEqual(actual, expect)