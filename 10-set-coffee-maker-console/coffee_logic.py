from coffee_menu import MENU, resources


#method to display resource report

def display_report(money_made):
    
    print(f"Coffe Machine Resource Report:\n")
    
    for key, item in resources.items():
        
        print(f"{key.capitalize()}: {item}ml" if key != "coffee" else f"{key.capitalize()}: {item}g")
    
    print(f"Money: ${money_made}")    


#method to check for sufficient resources

def check_resources(drink_ingredients):
    
    for item in drink_ingredients:
        if drink_ingredients[item] < resources[item]:
            return True
        else:
            return False    
            
            


#method to deduct the requred ingredients from the resources
def deduct_resources(drink_ingredients):
    
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]