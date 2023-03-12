class Hangman():
    
    def __init__(self, word):
        self.word = word
        self.guessed = []
        self.tries = 0
        self.maxtries = 6
        self.done = False
        self.won = False
    
    def guess(self, letter):
        if letter in self.guessed:
            return "You already guessed that letter."