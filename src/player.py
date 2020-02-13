# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []
    
    def __repr__(self):
        return f"\033[35m{self.name} is currently exploring: {self.location}"

    def pick_up(self, the_item):
        for item in self.location.items:
            if the_item in item.name:
                self.items.append(item)
                self.location.items.remove(item)
                print(f"You have picked up {item.name}")
            else:
                print("That item is not in your current location.")
    
    def put_down(self, the_item):
        for item in self.items:
            if the_item in item.name:
                self.location.items.append(item)
                self.items.remove(item)
                print(f"You have put down {item.name}.")
            else:
                print("That item is not currently in your player's backpack")
