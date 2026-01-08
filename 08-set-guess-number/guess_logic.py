import random

#method to generate a random number

def generate_random_number():
    return random.randint(1,100)

def difficulty_setting():
    
    guess_attempts = 0
    #prompting user for the number of attempts 
    user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        
    # if statement to set attempts based on user choice
    if user_choice == 'easy':
            guess_attempts = 10
    elif user_choice == 'hard':
            guess_attempts = 5
    else:
        print("Invalid choice. Please choose 'easy' or 'hard'.")
        difficulty_setting()        
            
    return guess_attempts    