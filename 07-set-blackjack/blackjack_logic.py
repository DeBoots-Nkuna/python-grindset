import random


#variable declaration
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []


#method to draw card
def deal_card():
    
    #calling method to clear cards
    clear_cards()
    #for loop to draw two cards each for user and computer
    for _ in range(2):
        
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        
    return user_cards, computer_cards


#method determine blackjack
def check_blackjack(user_hand, pc_hand):
    
    #if statement to check if user has ace and 10 or pc has ace and 10
    if user_hand == [11,10] and sum(user_hand) == 21:
        return "You have a Blackjack. You win!"
    
    elif pc_hand == [11,10] and sum(pc_hand) == 21:
        return "Computer has a Blackjack. You lose!"


#method to calculate score
def calculate_score(user_hand, pc_hand):
    
        user_score = sum(user_hand)
        pc_score = sum(pc_hand)
        return user_score, pc_score


#method to determine winner
def compare_score(user_score, pc_score):
    
    if user_score > 21:
        return "You went over. You lose!"
    elif pc_score > 21:
        return "Computer went over. You win!"
    elif user_score > pc_score and user_score <= 21:
        return "You win!"
    elif pc_score > user_score and pc_score <= 21:
        return "You lose!"


def add_user_card(user_hand):
    user_hand.append(random.choice(cards))
    return user_hand

def add_pc_card(pc_hand):
    # if statement
    if sum(pc_hand) < 17:
        pc_hand.append(random.choice(cards))
        return pc_hand

#method to clear cards
def clear_cards():
    user_cards.clear()
    computer_cards.clear()
    

#method to display current hands
def display_hands(user_hand, pc_hand):
    print(f"Your cards: {user_hand}, current score: {sum(user_hand)}")
    print(f"Computer's first card: {pc_hand[0]}")