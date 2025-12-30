from cipher_art import logo
from cipher_logic import message_cipher

#variable declaration
program_running = True


#displaying program logo
print(logo)


#while loop to keep program running until users decides to exit

while program_running:
    
    #prompting user for input
    program_choice = input("Type 'encode' to encrypt, or type 'decode' to decrypt:\n").lower()
    
    #if statement to check if user input is encode or decode
    if program_choice == 'encode' or program_choice == 'decode':
        
        #prompting user for message and shift number
        user_message = input("\nType the message you want to encrypt/decrypt:\n").lower()
        shift_number = int(input("\nType the number of shifts you. want to apply:\n"))
        #calling method to process the message
        output_result =message_cipher(original_message= user_message, shift_amount = shift_number, cipher_option = program_choice)
        
        #displaying the output result
        print(f"The {program_choice}d message is: {output_result}")        
        
    else:
        print("\nYou typed an invalid option. Please try again.\n")
        continue
    
    
    #prompting user if they want to continue or exit the program
    user_choice = input("\nType 'yes' if you want to continue. Otherwise type 'no' to exit.\n").lower()
    
    #if statement
    if user_choice == 'yes':
        continue
    elif user_choice == 'no':
        program_running = False
        print("\nTill next time. Goodbye!")
    else:
        program_running = False
        print("\n You typed an invalid option. Exiting the program.\n Goodbye!")
        
            
        
        

