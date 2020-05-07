from room import Room
from player import Player
from os import system
from item import items


def clear(): return system('cls')

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


room['treasure'].adjustItems('add', items['Sunlight Straight Sword'])
room['overlook'].adjustItems('add', items['Small Friend'])
room['foyer'].adjustItems('add', items['Rope'])
room['narrow'].adjustItems('add', items['Rusted Key'])
room['outside'].adjustItems('add', items['Heavy Rock'])

# print('Items outside:', room['outside'].items)


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Tyler', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def searchRoom(itemsInRoom):
    # print('current items:', itemsInRoom)
    if len(items) == 0:
        print("You scan the room but find nothing of use")
    else:
        print("You scan the room and see the following: ")
        for i in itemsInRoom:
            print(
                f"\n--------------------------------------------------------------------------------\n1x {i} \n{items[i].description}\n--------------------------------------------------------------------------------\n")


# def manipulateItems(action, item):


def validateDirection(nextRoom):
    if nextRoom:
        player1.current_room = nextRoom
        print(
            f"You travel to \n[{nextRoom.name}] \n\n--------------------------------------------------------------------------------\n{nextRoom.description}\n--------------------------------------------------------------------------------\n\n")
    else:
        print('Not a valid direction!\n')


def manageInventory(action, item):
    clear()
    if action.lower() == 'get':

        for i in player1.current_room.items.copy():
            # print('KEYWORD', player1.current_room.items[i].keyword)
            if item.lower() == player1.current_room.items[i].keyword:
                
                player1.adjustInventory('add', player1.current_room.items[i])
                player1.current_room.adjustItems('remove', player1.current_room.items[i])
                print(f"\nYou picked up the {item}")
            else:
                print("No such item exists!")

    elif action.lower() == 'drop':

        for i in player1.inventory.copy():
            if item.lower() == player1.inventory[i].keyword:
                player1.current_room.adjustItems('add', player1.inventory[i])
                player1.adjustInventory('remove', player1.inventory[i])
                print(
                    f"\nYou dropped the {player1.current_room.items[i].keyword} in the {player1.current_room.name}")
            else:
                print("No such item exists!")



clear()
print("\nWelcome adventurer! To the North you see a mysterious cave entrance...\n")

while True:
    entry = input(
        "What will you do? \n\nMove: Type [N] [S] [E] [W] \n\n[Search] = Look Around  [I] = Manage Inventory  Quit = [Q]")
    entry = entry.lower()
    print('\n')
    clear()

    print('Entry:', str(entry))

    if entry == 'q':
        print("Thanks for playing!\n")
        break

    elif entry == 'i':
        availableItems = player1.current_room.items
        for i in availableItems:
            print(
                f"\n--------------------------------------------------------------------------------\n1x {i} \n{items[i].description}\n--------------------------------------------------------------------------------\n")

        choice = input(
            'Manage inventory: Type [GET]/[DROP] [ITEM NAME]:').split(' ')
        action = choice[0]
        item = choice[1]

        print('ACTION/CHOICE', action, choice)
        manageInventory(action, item)

    elif entry == 'search':
        availableItems = player1.current_room.items
        searchRoom(availableItems)

    elif entry == 'n':
        nextRoom = player1.current_room.n_to
        validateDirection(nextRoom)

    elif entry == 's':
        nextRoom = player1.current_room.s_to
        validateDirection(nextRoom)

    elif entry == 'e':
        nextRoom = player1.current_room.e_to
        validateDirection(nextRoom)

    elif entry == 'w':
        nextRoom = player1.current_room.w_to
        validateDirection(nextRoom)

    else:
        print("Not a valid direction!")
