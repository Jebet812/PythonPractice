import random

def guess(x): 
    
    random_number = random.randint(1,x)
    guess = 0
    
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        
        if guess < random_number:
            print("The guess is too low. Kindly guess again.")
        
        elif guess > random_number:
            print("The guess is too high. Kindly guess again.")
            
    
    print(f"Congratulations. You win a prize for guessing\
        the correct number {random_number}.")
    
guess(10)