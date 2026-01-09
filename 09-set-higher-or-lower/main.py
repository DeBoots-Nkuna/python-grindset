from higher_art import logo, vs
from higher_logic import get_data, checking_data


#displaying the game logo
print(logo)


#varaible declaration
program_running = True
user_points = 0
temp_profile = {}

while program_running:
     
    #collecting the data
    # if statement
    if user_points == 0 and temp_profile == {}:
        profile1 = get_data()
    
    profile2 = get_data()
    
    #checking if we have duplicate profiles
    if profile1 == profile2:
        profile2 = get_data()
    
     
     #displaying the data
    print(f"\nCompare A: {profile1['name']}, a {profile1['description']}, from {profile1['country']}\n")
     
     #displaying vs logo
    print(vs)
     
    print(f"\nAgainst B: {profile2['name']}, a {profile2['description']}, from {profile2['country']}\n")
     #prompting user for a guess
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
     
     #if statement
    if user_choice == 'a' and profile1["follower_count"] > profile2["follower_count"]:
        user_points += 1
        print(f"You are correct! Your current score is {user_points}")

        #changing profile 1 to profile 2 and getting a new profile
        temp_profile = profile2
        profile1 = temp_profile
        print("\n" * 10)
    elif user_choice == 'b' and profile2["follower_count"] > profile1["follower_count"]:
        user_points += 1
        print(f"You are correct! Your current score is {user_points}")
        temp_profile = profile1
        profile1 = temp_profile
        print("\n" * 10)
    elif user_choice != 'a' and user_choice != 'b':
        print("Invalid choice. Please type 'A' or 'B'.")
        program_running = False
        break
    else:
        program_running = False
        print(f"Sorry, that's wrong. Your final score is {user_points}")    
        
        

    