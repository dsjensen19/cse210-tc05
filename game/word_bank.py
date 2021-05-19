import random
class Word_bank():
  #phrases = string[]
  #active_phrase = string

    #pick a random word from the bible dictionary
    
    # Open the file in read mode
    with open("BD.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
    
        # print random string
        


    def choose_active_Phrase(words):
        word = (random.choice(words))
        while len(word) <=2 or len(word) >= 10:
            word = (random.choice(words))
        print(word)
    """
    def check_letter():
        pass
    def display():
        pass
    """