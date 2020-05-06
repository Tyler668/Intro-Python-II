from room import Room
from player import Player
from os import system


clear = lambda: system('cls')

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


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
player1 = Player('Tyler', room['outside'])


def validateDirection(nextRoom):
    if nextRoom:
        player1.current_room = nextRoom
        print(
            f"You advance to \n[{nextRoom.name}] \n\n{nextRoom.description}\n\n")
    else:
        print('Not a valid direction!\n')


print("\nWelcome adventurer! North of you stands a mysterious cave entrance...\n")

while True:
    entry = input("Where will you go? [N], [S], [E], [W], Quit = [Q]")
    print('\n')

    # print('Entry:', entry)
    # print('Current room:', player1.current_room.name)

    if entry == 'Q' or entry == 'q':
        clear()
        print("Thanks for playing!\n")
        break

    elif entry == 'N' or entry == 'n':
        clear()
        nextRoom = player1.current_room.n_to
        validateDirection(nextRoom)

    elif entry == 'S' or entry == 's':
        clear()
        nextRoom = player1.current_room.s_to

        validateDirection(nextRoom)

    elif entry == 'E' or entry == 'e':
        clear()
        nextRoom = player1.current_room.e_to

        validateDirection(nextRoom)

    elif entry == 'W' or entry == 'w':
        clear()
        nextRoom = player1.current_room.w_to

        validateDirection(nextRoom)

    else:
        clear()
        print("Not a valid direction!")

   
