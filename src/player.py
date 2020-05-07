# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item


class Player:
    def __init__(self, name, current_room, inventory = None):
        self.name = name
        self.current_room = current_room
        self.inventory = {}

    def __str__(self):
        return f"{self.name} is in room {self.current_room}"

    def adjustInventory(self, action, item):
        if action == 'add':
            self.inventory.update({item.name : item})
        elif action == 'remove':
            del self.inventory[item.name]
