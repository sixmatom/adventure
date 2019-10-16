import unittest

import game


class GameTest(unittest.TestCase):
    def test_create(self):
        g = game.Game(name="Testgame")
        self.assertTrue(str(g), "Testgame")
