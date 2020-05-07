# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, items = None, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.items = {}
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def adjustItems(self, action, item):
        if action == 'add':
            print(f'Adding to {self.name}:', item.name)
            self.items.update({item.name : item})
        elif action == 'remove':
            del self.items[item.name]

