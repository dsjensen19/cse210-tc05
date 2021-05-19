import random

with open("BD.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.splitlines()))

class Word_bank():
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Rabbit): An instance of rabbit.
    """
        self.active_phrase = ""
        self.distance = [0, 0]
  #active_phrase = string

    #pick a random phrase from the bible dictionary
    
    # Open the file in read mode
    
        self.words = words
        
    
        # print random string
    
        


    def choose_active_Phrase(self,):
        active_phrase = (random.choice(words))
        while len(active_phrase) <=2 or len(active_phrase) >= 15:
            active_phrase = (random.choice(words))
            active_phrase.replace(""," ")
        #print("choose " +active_phrase)
        self.active_phrase = active_phrase
    
    
    def check_letter(self):
        #from game.player import guesses
        guesses = ['a','e','i','o','f','g']
        for c in self.active_phrase:
            if c in guesses:
                print(c)
                #so how do I implement this with display so it shows the characters in this list on the lines from display?
                #I'm just a bit confused as to how its split vs nto just doing it all in one function
        pass
    
    def display(self):
        for c in self.active_phrase:
            print("_",end = "")
        print()
