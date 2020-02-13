class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return  f"{self.name} + '\n' + {self.description}"

    def on_grab(self):
        print(f"You've snatched up {self.name}")
    
    def on_drop(self):
        print(f"You tossed {self.name}")
