import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  #this will choose a random list from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
        
    return(word)

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has guessed
    
    #get user input
    while len(word_letters) > 0:
        # letters used
        # ' '.join({'a', cd,}) --> 'a, cd'
        print("You have guessed these letters: ", ' '.join(used_letters))
        
        # what current word is with dashes where unguessed letters are (W - R -D)
        word_list = [letter if letter in used_letters else  '-' for letter in word]
        print("Current word: ", ' '.join(word_list))
        
        
        user_letter =  input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
        elif user_letter in used_letters:
            print("That character has been used. Please try again.")
        
        else:
            print("You have not typed in a valid character. Kindly try again.")
            
        
    #gets here when len(word_letters) == 0   
user_input = input("Type something: ")
print(user_input)
    
        