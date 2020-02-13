# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    '''
    This is a room class
    '''
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.items =[]
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        '''
        This is a string method
        '''
        return f"{self.title}\n\n{self.description}\n\n{self.items}"