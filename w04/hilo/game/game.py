import player
import card

class Game:

    def __init__(self):

        self.isPlaying = True

        self.start_game()


    def start_game(self):

        player1 = player.Player()

        """
        An intance of player is created.
        The game is set to play
        """

        while self.isPlaying:
            """
            The game will continue as the player has > 0 points
            and decides to keep playing.
            """
            self.play(player1)
            self.end_game(player1)

                #The new card is now the Player's card.



    def play(self, player1):
        player1.display_card()
        #The current card is deplayed

        guess = input("Higher or lower? [h/l] ")
        if guess.lower() != "h" and guess.lower() != "l":
            print("Incorrect entry, please use 'h' or 'l'.")
        else:
            new_card = card.Card()
            print(f"Next card was: {new_card.get_number()}")
            """
            The new card is stores and displayed.
            """

            if guess.lower() == "h":
                if new_card.get_number() > player.card.get_number():
                    self.change_points(player,True)
                else:
                    self.change_points(player,False)
            elif guess.lower() == "l":
                if new_card.get_number() < player.card.get_number():
                    self.change_points(player,True)
                else:
                    self.change_points(player,False)

            """
            The new card is compared with the current card, if played guessed correctly point are added, if not substracted. If it has the same value, nothing happens.

            """        

            player1.card = new_card
            

    def change_points(self, player1, guess):
        """Updates the player's score according to the accuracy of their guess

        Args:
            self (Player): An instance of Player.
        """
        if guess==True:
            player1.points+=100
        elif guess==False:
            player1.points-=75

    def end_game(self, player1):
        if player1.points <= 0:
            player1.points = 0
            self.isPlaying=False
            print("You ran out of point to play.")

            """
            In order to be more visual appealing the score will not go under 0.
            """

            player1.display_points()   
            #points displayed.
        if player1.points != 0:
            while True:  
                play = input("Play again? [y/n] ")
                if play.lower() != "y" and play.lower() != "n":
                    print("Incorrect entry, please use 'y' or 'n'.")
                else:
                    if play.lower() == "y":
                        self.isPlaying=True
                    elif play.lower() == "n":
                        self.isPlaying=False
                    break

        print("Thanks for playing!")


        