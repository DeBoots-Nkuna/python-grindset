from calculator_art import logo
from calculator_logic import operations_dict
#displaying programs logo
print(logo)


#declaration of named functions
addition = operations_dict["+"]
subtraction = operations_dict["-"]
multiplication = operations_dict["*"]
division = operations_dict["/"]
program_running = True
total = 0


#while loop

while program_running:

    if total == 0:
        #prompting user for inputs
        num1 = float(input("Enter first number: "))
        
    #prompting user to choose an operation
    operation_sign = input("Choose an operation:\n+\n-\n*\n/\n")

    #if statements
    if operation_sign == "+":
        num2 = float(input("Enter second number: "))
        total = addition(num1, num2)
        print(f"{num1} + {num2} = {total}")
    elif operation_sign == "-":
        num2 = float(input("Enter second number: "))
        total = subtraction(num1, num2)
        print(f"{num1} - {num2} = {total}")

    elif operation_sign == "*":
        num2 = float(input("Enter second number: "))
        total = multiplication(num1,num2)
        print(f"{num1} * {num2} = {total}")
        
    elif operation_sign == "/":
        num2 = float(input("Enter second number: "))
        total = division(num1, num2)
        print(f"{num1} / {num2} = {total}")
    else:
        print("You have entered an incorrect operation sign. Please try again.")
        program_running = False
        break
    
    #prompting user if they want to continue calculating with the current total
    user_choice = input(f"Type 'yes' to continue calculating with {total}, or type 'new' to start a new calculation or exit to end the program? : ").lower() 
    
    if user_choice == 'yes':
        print("\n" * 35)
        continue
    elif user_choice == 'new':
        total = 0
        continue
    elif user_choice == 'exit':
        program_running = False
        print("Thank you for using the calculator. Goodbye!") 
    else:
        program_running = False
        print("You have entered an invalid choice. Exiting the program.")           
