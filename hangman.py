import random
from words import word_list
def get_word():
    word  = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("let's play hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
