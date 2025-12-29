import random
from hangman_art import logo, stages
from hangman_logic import select_category, select_riddle

#display game logo and welcome message
print(logo)
print("\n\nWelcome to Hangman Game with a Twist! 🎭🪓\n\n")

#variables to track game state
game_over = False
user_lives = 6
riddle_chances = 2
correct_guess_list = []
word_length = 0
display = ""

#while loop

#prompt user to choose the words category
user_choice = input("\nChoose a category for the secret word. Type (animals, sports, movies, general, food, entertainment, nature, technology or space):\n\n").lower()

#calling function to select category
word_list = select_category(user_choice)

if word_list:
    secret_word = random.choice(word_list)
    
    #collecting the word length
    word_length = len(secret_word)
    
    #displaying info to user
    print(f"\nYour category selection is '{user_choice}'. The secret word has {word_length} letters.\n\n")
    
    #creating the initial place holder
    place_holder = "_" * word_length
    print(f"\n {place_holder}\n")
else:
    print("\n\nYou entered an incorrect category. Please restart the game and choose a correct cateory.\n\n")
    game_over = True   

# initialising temp list of correct guesses
correct_guesses_list = ["_"] * word_length 

#main game loop
while game_over != True:
        #prompting user to guess the letter
        user_guess = input("Guess a letter:\n\n").lower()
        
        
        #checking if the user has already guessed the letter    
        if user_guess in correct_guesses_list:
                
            print(f"\nYou have already guessed the letter '{user_guess}'. Try a different letter.\n")
            continue  
        
        
        #for loop
        for index, letter in enumerate(secret_word):
            
            #if statement
            if letter == user_guess:
                
                #update the correct letter in the temp list
                correct_guesses_list[index] = user_guess
                
        # display the current state of correct word , hangman art and lives left
        display = "".join(correct_guesses_list)
        print(f"\nWord Progress: {display}\n")   
            
        #checking if user guessed a letter that is not in the secret word
        if user_guess not in secret_word:
                
            #reducing user lives by 1
            user_lives -= 1
            print(f"\n\nThe letter you guessed '{user_guess}, is not part of the secret word. You lost a life.\n\n")  
                
        
        
        #if statemens to check if display matches secrete word and if user lives is 0 
        if display == secret_word:
            print(f"######################## You Won! The secret word is '{secret_word}' ########################\n")
            game_over = True
            
        #cchecking if user lives is 0 to end the game
        if  user_lives == 0:
            print(f"######################## You Lost! The secret word was '{secret_word}' ########################\n")
            game_over = True
        
        #displaying game info to user
        print(stages[user_lives])
        print(f"######################## Remaining Lives: {user_lives} ########################\n")
           
        
        # checking if user lives is 1 to prompt for a riddle challenge
        if user_lives == 1 and riddle_chances > 0:
            
            #displaying info to user
            print(f"\nLast Chance!🚨 You have {user_lives} life left. Solve the riddle to reclaim +2 lives.\n\n")
            
            #calling function to retrieve riddle
            riddle_question, riddle_answer = select_riddle()
            
            #displaying riddle to user
            print(f"Riddle: {riddle_question}\n")
            user_answer = input("Your Answer: ").lower()
            
            #checking i user answer is correct
            if user_answer == riddle_answer:
                
                #updating user lives
                user_lives += 2
                #reducing riddle chances by 1
                riddle_chances -= 1
                
                print(f"\n Correct Answer! You have been awarded 2 extra lives. You now have {user_lives} lives remaining.\n")
                print(f"\nWord Progress: {display}\n")
                continue
            else:
                print(f"\n Wrong Answer! The correct answer was '{riddle_answer}'. You still have {user_lives} life remaining.\n")
                
                #reducting riddle chances by 1
                riddle_chances -= 1
                
                #displaying the current word
                print(f"\nWord Progress: {display}\n")
                continue
        elif user_lives == 1 and riddle_chances == 0:
            print(f"\nNo riddle chances left.🥹 You have {user_lives} life remaining. Good luck!🙇‍♂️\n")
            continue
           
            
        
                
        
                

