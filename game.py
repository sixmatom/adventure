import json


class Game:
    def __init__(self, name, commands=None):
        self.name = name
        pass

    def __str__(self):
        return self.name
