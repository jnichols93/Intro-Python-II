# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []
    def travel(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction")

    
    def get_item(self, pickup_item):
        self.items.append(pickup_item)

    def drop_item(self, drop_item):
        self.items.remove(drop_item)
        self.current_room.items.append(drop_item)

    def __str__(self):
        return f'{self.name} is in the {self.current_room}. \n {self.current_room.description}'