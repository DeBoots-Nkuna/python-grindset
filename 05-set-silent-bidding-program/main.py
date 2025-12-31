from bidding_art import logo
from bidder_logic import determining_bid_winner

#displayng the program logo
print(logo)

#variuable declarations
program_running = True
silent_bidding = {}


#while loop

while program_running:
    
    #prompting user for name and their bid amount
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: R"))
    
    #adding info to the dictionary
    silent_bidding[user_name] = user_bid
    
    
    #prompting user if there are any other bidders to continue or end the bidding 
    user_choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    
    #if statement to check if user choice is yes or no
    if user_choice == 'yes':
        continue
        print("\n" * 30) #clearing the console for the next bidder
        
    elif user_choice == 'no':
        
        program_running = False
        
        #calling function to determine the highest bidder  
        highest_bidder_name, highest_bid_amount =  determining_bid_winner(silent_bidding)
        
        #displaying the highest bidder info
        print(f"The highest bidder is {highest_bidder_name} with a bid of R{highest_bid_amount}")
        
    else:
        print("You have entered an invalid choice. Ending the bidding..")
        program_running = False
        

             