# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    
    def __repr__(self):
        return '\033[93m'+ self.name + '\n' +'\033[96m'+ self.description + '\n' + str(self.items)