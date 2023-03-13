import random


class Hangman():

    @staticmethod
    def choose_random_word():
        with open("words.txt", "r") as f:
            words = f.read().splitlines()
            return random.choice(words)
    
    def __init__(self, author, word):
        self.author = author
        self.word = word
        # print(self.word)
        self.guessed = []
        self.lives = 0
        self.maxlives = 6
        self.done = False

    def start_up(self):
        return f"Welcome to Hangman {self.author.mention}! For all the hangman commands, type `!pasta hangman` at any time.\nYour word is {len(self.word)} letters long, and looks like this: {self.print_current_guessed_word()}\nYou have {self.maxlives - self.lives} lives left.\nWhat's your first guess?"
    
    def print_guesses_and_lives(self):
        return f"Mystery word: {self.print_current_guessed_word()}\nGuesses: {self.print_current_guess()}\nLives left: {self.maxlives - self.lives}"
    
    def guess(self, letter):
        if letter in self.guessed:
            return f"You already guessed that letter {self.author.mention}. Try again!\n" + self.print_guesses_and_lives()
        
        self.guessed.append(letter)

        if letter in self.word:
            if self.check():
                self.done = True
                return f"You finished the word {self.author.mention}! The word was {self.word}!\nYou did it with {self.maxlives - self.lives} lives left! Nice work {self.author.nick}! The game is now over."
            else:
                return f"Correct {self.author.mention}! '{letter}' is in the word.\n" + self.print_guesses_and_lives() + "\nWhat's your next guess?"
        else:
            self.lives += 1
            if self.lives == self.maxlives:
                self.done = True
                return f"You lost {self.author.mention}! The word was {self.word}.\nThanks for playing!"
            else:
                return f'''Incorrect {self.author.mention}! '{letter}' is **not** in the word.\n" + self.print_guesses_and_lives() + "\nWhat's your next guess?'''

    
    def check(self):
        for letter in self.word:
            if letter not in self.guessed:
                return False
        return True
    
    def print_current_guessed_word(self):
        current_guess = ""
        for letter in self.word:
            if letter in self.guessed:
                current_guess += letter
            else:
                current_guess += "\_"
        print(current_guess)
        return current_guess
    
    def print_current_guess(self):
        return ', '.join(self.guessed)
    
    def end(self):
        return f"You have ended the game {self.author.nick}. The word was {self.word}."
