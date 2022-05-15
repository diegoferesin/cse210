from card import Card
class Player:
    """
        The player starts the game with 300 points
        and will draw cards and guess if the next card
        will be higher or lower than the previous; the 
        player will earn or lose points according to the
        accuracy of their guess.
        Attributes:
            points (int): keep track of the player's success in the game
    """
    def __init__(self):
        self.points = 300
        self.card = Card()
        '''
        Constructs a new instance of Player with a points and a card attribute.
        Args:
            self (Player): an instance of a Player
        '''

    def get_points(self):
        '''
        Returns the current value of the points attribute
        Args:
            self (Player): an instance of a Player
        '''
        return self.points



    def display_points(self):
        '''
        Displays the current number of points of the player

        Args:
            self (Player): An instance of Player.
        '''
        print(f"Your score is: {self.get_points()}")

    def display_card(self):
        '''
        Displays the player's card's value 

        Args: 
            self (Player): An instance of Player
        '''
        self.card.display_number()
