import json
import sys

from location import Location


class Game:
    def __init__(self, name, locations=None, commands=None):
        self.name = name
        self.locations = [Location(**location) for location in (locations or [])]

    def __str__(self):
        return self.name

    @classmethod
    def load(cls, filename):
        print('Loading game "%s"' % filename)
        with open(filename) as fin:
            data = json.load(fin)
        return Game(**data)

    def run(self):
        print('Running game "%s"' % self)


if __name__ == "__main__":
    try:
        game = Game.load(sys.argv[1])
        game.run()
    except IndexError:
        print("Usage: %s <game.json>" % sys.argv[0])
