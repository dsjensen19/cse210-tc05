from game.player import Player
from game.parachute import Parachute
from game.word_bank import Word_bank
class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        hunter (Hunter): An instance of the class of objects known as Hunter.
        rabbit (Rabbit): An instance of the class of objects known as Rabbit.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
      
        self.player = Player()
        self.keep_playing = True
        self.parachute = Parachute()
        self.word_bank = Word_bank()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self.word_bank.choose_active_Phrase()
        self.word_bank.display()
        self.parachute.display()
        while self.keep_playing:
            self.take_turn()



    def take_turn(self):
        """Gets the guess from the player
        """
        guess = self.player.guess_letter()

        if (self.word_bank.check_letter(guess)):
            self.guessed_correctly()
        else:
            self.guessed_incorrectly()

        
        
    def guessed_correctly(self):
        """runs the functions for when the player guessed correctly

        Args:
            self (Director): An instance of Director.
        """
        if self.word_bank.has_won():
            self.word_bank.display()
            self.parachute.display()
            print("You got it!!!!!!!!")
            self.keep_playing = False
        else:
            self.word_bank.display()
            self.parachute.display()
        
    def guessed_incorrectly(self):

        self.word_bank.display()
        self.parachute.cut_layer()

        if(self.parachute.can_cut_layer()):
            self.parachute.display()
        else:
            self.parachute.display()
            print("Game Over!")
            print("The word was: "+ self.word_bank.active_phrase)
            self.keep_playing = False
            
