from guess_art import logo
from guess_logic import generate_random_number, difficulty_setting
import random
#displaying logo for the program
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = generate_random_number()
programm_running = True
guess_attempts = 0



#setting difficulty level for the first time
guess_attempts = difficulty_setting()

#while loop to run the guessing game
while programm_running:
    
    
    print(f"You have {guess_attempts} attempts remaining to guess the number.")          
    user_guess = int(input("Make a guess: "))
    
    #if statement to check the guess
    if user_guess > random_number:
        print("Too High.")
        guess_attempts -= 1
    elif user_guess < random_number:
        print("Too Low.")
        guess_attempts -= 1
    else:
        print(f"Bingo! You guessed the number {random_number} correctly!")
        programm_running = False
      
              
    if guess_attempts == 0:
        programm_running = False
        print("You've ran out of guesses. You lose. Goodbye!")
               