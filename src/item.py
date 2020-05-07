


class Item:
    def __init__(self, name, description, keyword):
        self.name = name
        self.description = description
        self.keyword = keyword
    



items = {
    'Heavy Rock': Item('Heavy Rock', 'An imposing and jagged stone, to lift it would test the limits of your strength', 'rock'),
    'Rope' : Item('Rope', 'A pile of coiled rope, of questionable tensile strength', 'rope'),
    'Small Friend' : Item('Small Friend', 'A peculiar ball of fur, he radiates positivity', 'friend'),
    'Rusted Key' : Item('Rusted Key', 'A key to an unknown door, oxidized and fragile', 'key'),
    'Sunlight Straight Sword' : Item('Sunlight Straight Sword', 'A dazzling and ornate blade, warm to the touch.', 'sword'),
    'Suspicious Stew' : Item('Suspicious Stew', "A strange colored stew, I'd never eat such a thing... Unless?", 'stew')
}

