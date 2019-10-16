import json

from item import Item


class Location:
    def __init__(self, name, description=None, items=None):
        self.name = name
        self.description = description or ""
        self.items = [Item(**item) for item in (items or [])]

    def __str__(self):
        return self.name
