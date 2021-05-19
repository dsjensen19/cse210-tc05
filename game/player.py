class Player():
    def __init__(self):
        chosen_letters = []

    def guess_letter(self):
        guess = "da"
        while len(guess) != 1 and guess in self.chosen_letters:
            guess = str(input("Guess your letter a-z!"))
        self.chosen_letters.append(guess)  
        return guess

         