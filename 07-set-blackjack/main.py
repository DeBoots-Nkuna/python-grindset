from blackjack_art import logo
from blackjack_logic import deal_card, check_blackjack, calculate_score, compare_score, add_user_card, add_pc_card, display_hands


#displaying program logo
print(logo)


user_choice = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()


if user_choice == 'yes':
    
    #calling method to deal cards
    user_hand, pc_hand = deal_card()
    
    #invoking methods to check blackjack and calculate score
    blackjack_result = check_blackjack(user_hand=user_hand, pc_hand=pc_hand)
    user_score, pc_score = calculate_score(user_hand=user_hand, pc_hand=pc_hand)
    
    #displaying the user and pc cards

    display_hands(user_hand=user_hand, pc_hand=pc_hand)
    
    #prompting user if they want to draw another card or pass
    user_choice2 = input("Type 'yes' to draw another card, type 'no' to pass: ").lower()
    
    #if statement to check user choice
    if user_choice2 == 'yes':
        #invoking method to draw another card for both user and pc
        add_user_card(user_hand=user_hand)
        add_pc_card(pc_hand=pc_hand)
    elif user_choice2 == 'no':
        add_pc_card(pc_hand=pc_hand)
        
    #recalculating the scores after drawing another card 
    user_score, pc_score = calculate_score(user_hand=user_hand, pc_hand=pc_hand)
  
    #displaying final hands and scores
    display_hands(user_hand=user_hand, pc_hand=pc_hand)

    #determining the winner
    result = compare_score(user_score=user_score, pc_score=pc_score)
    print(result)

else:
    print("Maybe next time.Bye!")    