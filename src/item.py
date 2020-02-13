class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return  self.name + '\n' + self.description

# class Money(Item):
#     def __init__(self, name, description):
#         super().__init__(name, description)
#         self.category = money

# class Tools(Item):
#     def __init__(self, name, description):
#         super().__init__(name, description)
#         self.category = tools

# class Weapon(Item):
#     def __init__(self, name, description):
#         super().__init__(name, description)
#         self.category = weapon