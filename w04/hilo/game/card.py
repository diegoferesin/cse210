import random
class Card:
    def __init__(self):
        self.number = random.randint(1,13)
    """
    Individual cards are represented as a number from 1 to 13.
    Attributes:
        number (int): The value of the card
    """
    def get_number(self):
        '''
        Return the value of the card
        '''
        return self.number
    
    def display_number(self):
        print(f"The card is: {self.get_number()}")
    """
    This method will display the number obtained by the set_number method.
    """