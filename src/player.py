# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def __repr__(self):
        return f"\033[35m{self.name} is currently exploring: {self.location}"