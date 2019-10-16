import unittest

from location import Location


class LocationTest(unittest.TestCase):
    def test_create(self):
        location = Location(name="Woonkamer")
        self.assertTrue(str(location), "TestgWoonkamerame")

