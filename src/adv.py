from room import Room
from player import Player
from item import Item, Food, Egg
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
    'treasure':   Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
    'greatHall':    Room("Great Hall", """You see a great room with a throne. the door shuts and locks behind you. Above the throne
 you see a glint of something. The only exit is to the south."""),
    'forest':   Room("Forest", """you start to see light as you exit a cave and greenery
 and fresh air hit you as you exit. you've made it out congratulations""" ),
}

items = {
    "bow": Item("bow", "a bow, now I need arrows."),
    "potato": Item("potato", "a potato...boil'em mash'em, put em in a stew."),
    "bread": Item("bread", "I'm deep in this dungeon, how did fresh bread end up here?!"),
    "glint": Item("glint", "You see a quiver of golden arrows on the wall above the throne")
}

# add items to rooms
room["foyer"].items = [items["bow"]]
room["overlook"].items = [items["potato"]]
room["treasure"].items = [items["bread"]]
room["greatHall"].items = [items["glint"]]

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['narrow'].w_to = room['greatHall']
room['greatHall'].s_to = room['forest']
# creates items

# Main

# Make a new player object that is currently in the 'outside' room.
player = Player(input("Name thy self: "), room['outside'])
print("You can go:", player.current_room)
print("You are currently: ", player.current_room.name)
print(player.current_room.description)

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

valid_directions = ("n", "s", "e", "w")

while True:
    player.display_items()
    cmd = input("\n~~> ")
    if cmd == "q":
        print("faire thee well!")
        exit(0)
    elif cmd in valid_directions:
        player.travel(cmd)
    elif cmd == "i":
        player.print_inventory()
    elif cmd.startswith("get") or cmd.startswith("take"):
        cmd_word = cmd.split()
        if len(player.current_room.items) > 0 and player.current_room.show_items(cmd_word[1]):
            player.take_item(items[cmd_word[1]])
        else:
            print(f"This room doesn't have a {cmd_word[1]}")
    elif cmd.startswith("drop"):
        cmd_word = cmd.split()
        player.drop_item(cmd_word[1])
    else:
        print("I did not understand that command")