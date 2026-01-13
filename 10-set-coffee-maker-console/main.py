from coffee_art import logo
from coffee_menu import MENU
from coffee_logic import display_report, check_resources, deduct_resources



#displaying logo program
print(logo)

#variable declaration
is_on = True
can_make_coffee = True
is_sufficient = True
money_made = 0.0
#TODO:Turn off the coffee machine by entering "off" to the prompt.
while is_on:
    #TODO: prompt user what would they like
    user_choice = input("\nWhat would you like? (espresso , latte, or cappuccino): ").lower()
    
    if user_choice == 'off':
        is_on = False
        print("Turning off the coffee machine. Goodbye!")
    elif user_choice == 'report':
        
        #invoking method to display report
        #TODO: Print the report when the user enters "report" to the prompt.
        display_report( money_made)
    elif user_choice in MENU:
        
        #collectng drink details from menu
        drink = MENU[user_choice]
        
        #checking for sufficient resources
        is_sufficient = check_resources(drink["ingredients"])
        
        #if statement to check if the resources are sufficient to make the drink
        #TODO: Check for sufficient resources to make the selected drink.
        if is_sufficient:
            
            #TODO: Prompt the user to insert coins, if there ae sufficient resources to make the drink.
            print("\nPlease insert coins.")
            
            #prompting the user to enter the number of coins
            num_quarters = int(input("How many quarters?: "))
            num_dimes = int(input("How many dimes?: "))
            num_nickels = int(input("How many nickels?: "))
            num_pennies = int(input("How many pennies?: "))
            
            
            #calculating the total amount paid by the user
            #TODO: Process the coinns. quarter = $0.25, dime = #0.10, nicke = $0.05, pennies = $0.01
            total_paid = (num_quarters * 0.25) + (num_dimes * 0.10) + (num_nickels * 0.05) + (num_pennies * 0.01)
            
            #checking if the user's payment is enough to cover the cost of the drink
            drink_cost = drink["cost"]
            
            if total_paid >= drink_cost:
                money_made += drink_cost
                change = round(total_paid - drink_cost, 2)
                print(f"Here is your change: ${change}")
                print(f"Here is your {user_choice} drink. Enjoy!")
            
            
            #TODO: deduct the required ingredients from the resources.
            deduct_resources(drink["ingredients"])

        else:
            is_on = False
            print("Cannot make the drink due to insufficient resources.")
    
    else:
        is_on = False
        print("You entered an invalid option. Turning off the coffee machine.\nGoodbye!")
            