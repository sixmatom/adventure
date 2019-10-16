import unittest

from game import Game


class GameTest(unittest.TestCase):
    def test_create(self):
        game = Game(name="Testgame", locations=[])
        self.assertTrue(str(game), "Testgame")

    def test_load(self):
        game = Game.load('data/simple_game.json')
        self.assertTrue(str(game), "Simple game")
