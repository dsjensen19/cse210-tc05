import random

with open("BD.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.splitlines()))

class Word_bank():
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
    """
        self.chosen_letters = [" "]
        self.active_phrase = ""
        active_phrase = self.choose_active_Phrase()
        self.distance = [0, 0]
        self.words = words
        self.guesses = []


    def choose_active_Phrase(self):
        active_phrase = (random.choice(words))
        while len(active_phrase) <=2 or len(active_phrase) >= 15:
            active_phrase = (random.choice(words))
            active_phrase.replace(","," ")
        #print("choose " +active_phrase)
        self.active_phrase = active_phrase
    
    
    def check_letter(self, guess):
        #from game.player import guesses
        self.chosen_letters.append(guess.lower())
        if guess in self.active_phrase:
            return True
        else:
            return False

    def display(self):
        for c in self.active_phrase.lower():
            if c in self.chosen_letters:
                print(c,end = "")
            elif c == " ":
                print(" ",end = "")
            else:
                print("_",end = "")
        print()
        
    def has_won(self):
        for c in self.active_phrase:
            if not (c in self.chosen_letters):
                return False
        print("You survived!")
        return True

