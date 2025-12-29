import random
from hangman_words import word_bank, riddles
from hangman_art import stages


#function to select the category the user wants

def select_category(user_choice):
    
    #if statement to check if user choice is valid
    if user_choice in word_bank:
        word_list = word_bank[user_choice]
        return word_list
    else:
        return None
    

#function to select a riddle
def select_riddle():
    
    #getting the length of the riddle list
    riddle_length = len(riddles) - 1
    riddle_question = ""
    riddle_answer = ""

    #choosing a random riddle
    riddle_choice = riddles.pop(random.randint(0, riddle_length))
    
    #constructing the riddle question and answer
    
    for key, value in riddle_choice.items():
        
        #if statement to verify key
        if key == 'q':
            riddle_question = value
        else:
            riddle_answer = value
            
    return riddle_question, riddle_answer

