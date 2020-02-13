from room import Room
from player import Player
# Declare all the rooms
from colorama import init
init()


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("The Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. although there appears to be something interesing twords the northern part of the room, The only exit is to the south."""),

'hidden': Room("Secret Passage", """You've found a secret passage leading north,
will you follow it?"""),

'tunnel': Room("Secret Tunnel", """The passage Leads to a tunnel heading west! The faint sound of music, more specifically Lou Bega's Mambo #5 can be heard hauntingly in the distance... do you dare proceed west?"""),

'den': Room("Strange Cavern", """The tunnel Leads you to a large cavern, the source of the ominous music now apparent. An i pad hooked up to a large boombox sits in the corner amongst a pile of treasure in the north of the room..."""),

'boombox': Room("The hobo encampment", """as you draw closer the faint smell of old Mc Donald's begins to permeate the air, the "treasure you thought you had found appears to be a bunch of garbage if im being honest... until you see it... a mix tape labeld mambo #6!!!!!!"""),
}

#declare all Items


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].n_to = room['hidden']
room['hidden'].s_to = room['treasure']
room['hidden'].n_to = room['tunnel']
room['tunnel'].e_to = room['hidden']
room['tunnel'].w_to = room['den']
room['den'].e_to = room['tunnel']
room['den'].n_to = room['boombox']
room['boombox'].s_to = room['den']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = input('What do you call yourself??? ~~~>')

player = Player(new_player, room['outside'])
print(player)



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
print('\033[92m'+'[n] North [e] EAST [s] SOUTH [w] WEST')
print('\033[39m') 

directions = input("~~~>")

def reset():
    print('\033[92m'+'[n] North [e] EAST [s] SOUTH [w] WEST')
    print('\033[39m') 
    global directions
    directions = input('~~~>')

    #def move(self, direction):
     #   if getattr(self.location, f'{direction}_to'):
      #  self.location = getattr(self.location, f'{direction}_to')
   # else:
    #    print('\033[31m'+'Your path is blocked!!')
     #   print('\033[39m') 

while not directions == "q":
  
    if directions == "w":
        try:
            player.location = player.location.w_to
            print(player)
        except:
            print('\033[31m'+'Your path is blocked!!')
            print('\033[39m') 
        reset()
    elif directions == "n":
        try:
            player.location = player.location.n_to
            print(player)
        except:
            print('\033[31m'+'Your path is blocked!!')
            print('\033[39m') 
        reset()
    elif directions == "e":
        try:
            player.location = player.location.e_to
            print(player)
        except:
            print('\033[31m'+'Your path is blocked!!')
            print('\033[39m') 
        reset()
    elif directions == "s":
        try:
            player.location = player.location.s_to
            print(player)
        except:
            print('\033[31m'+'Your path is blocked!!')
            print('\033[39m') 
        reset()
#item logic


print('\033[43m'+'\033[30m''Your adventure is over')
print('\033[39m') 
