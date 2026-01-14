from hydration_art import logo
from helper_logic import calc_water_intake


#displaying program logo
print(logo)


#prompting user to enter their weight in kg

user_weight = float(input("Enter your weight in kg: "))

#invoking method to calculate the water intake
result = calc_water_intake(user_weight)

#displaying result
print(f"You should drink about {result} liters of water per day.")
