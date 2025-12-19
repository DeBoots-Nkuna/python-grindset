import random

rock = '''

rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''

paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''

scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_hands = [rock,paper,scissors]
game_options = [0,1,2]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Papaer or 2 for Scissors: \n"))
computer_choice = random.choice(game_options)


if not user_choice in game_options:
    print("You choose a wrong option. You lose!")


#player hand display
if user_choice >= 0 and user_choice <= 2:
    print("Your hand:\n")
    print(game_hands[user_choice])

#computer hand display
print("Computer's hand:\n")
print(game_hands[computer_choice])

#determining winner

if user_choice == computer_choice:
    print("it's a tie!")
elif (user_choice == 0 and computer_choice == 2) or \
    (user_choice == 1 and computer_choice == 0) or \
    (user_choice == 2 and computer_choice == 1):
        print("You win!")
else:
    print("Computer win!")                