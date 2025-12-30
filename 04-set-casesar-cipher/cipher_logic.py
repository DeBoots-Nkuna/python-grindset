
#alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#method declaration to cipher the message
def message_cipher(original_message, shift_amount, cipher_option):
    
    ciphered_message = ""
    
    #if statement to check if the cipher option is decode
    if cipher_option == 'decode':
        shift_amount *= -1
        
    #for loop to iterate through each letter in the original message
    for letter in original_message:
        
        #if statement to check if letter exist in the alphabet list
        
        if letter in alphabet:
            
            #retrieving letter index position and adding the shift amount
            initial_index = alphabet.index(letter) + shift_amount
            
            #shifting the letter index position and handling index out of range to wrap around the alphabet list
            shifted_index = initial_index % len(alphabet)
            
            #retriving the new ciphered letter
            ciphered_message += alphabet[shifted_index]
        else:
            ciphered_message += letter    
    
    return ciphered_message            