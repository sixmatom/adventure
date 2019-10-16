import unittest

from item import Item


class ItemTest(unittest.TestCase):
    def test_create(self):
        item = Item(name="Woonkamer", description=None)
        self.assertEqual(str(item), "Woonkamer")
