import unittest

from game import Game


class GameTest(unittest.TestCase):
    def test_create(self):
        game = Game(name="Testgame")
        self.assertEqual(str(game), "Testgame")

    def test_load(self):
        game = Game.load("data/simple_game.json")
        self.assertEqual(str(game), "Simple game")
        self.assertEqual(len(game.locations), 1)
        self.assertEqual(str(game.locations[0]), 'woonkamer')
