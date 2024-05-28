# Seán Carroll
# Assignment Question 4
# Many companies use telephone numbers like 555-GET-FOOD so the number is easier for their customers to remember.
# On a standard telephone, the alphabetic letters are mapped to numbers in the following fashion.
# A,B,C = 2
# D,E,F = 3
# G,H,I = 4
# J,K,L = 5
# M,N,O = 6
# P,Q,R = 7
# T,U,V = 8
# W,X,Y,Z = 9
# Write a program that asks the user to enter a 10 character telephone number in the following format XXX-XXX-XXXX. 
# The application should display the telephone number with any alphabetic characters that appear in the original translated to their numeric equivalent . 
# Example - If the user enters 555-GET-FOOD , the application should display 555-438-3663

# Define the main function.
def main():

    # Prompt the user to enter a telephone number
    phone_number = input("Enter a 10-character telephone number (XXX-XXX-XXXX): ")

    # Go to the translate_to_numeric function. 
    # Bring the user's phone number.
    translate_to_numeric(phone_number)

    # Check if the input is in the correct format.
    if len(phone_number) == 12 and phone_number[3] == '-' and phone_number[7] == '-':
        
        # Call the phone number returned from the translate_to_numeric function translated_number so that it can be displayed.
        translated_number = translate_to_numeric(phone_number)
        
        # Display the translated_number.
        print('Translated number:', translated_number)
    
    # If the phone number was in the incorrect format display an invalid input message.
    else:
        
        print("Invalid input. Please enter a 10-character telephone number in the format XXX-XXX-XXXX.")

# Define the translate_to_numeric function. The user's phone number is brought to the function.
def translate_to_numeric(phone_number):
    
    # Initialise an empty string to store the numeric phone number
    numeric_phone = ""
    
    # For loop that checks each character in the input phone number.
    for character in phone_number:
        
        # Check if the character is an alphabet letter.
        if character.isalpha():
            
            # Convert the letter to uppercase for case-insensitivity.
            character = character.upper()
            
            # Assign each letter its corresponding numeric value.
            if 'A' <= character <= 'C':
            
                numeric_phone += '2'
            
            elif 'D' <= character <= 'F':
            
                numeric_phone += '3'
            
            elif 'G' <= character <= 'I':
            
                numeric_phone += '4'
            
            elif 'J' <= character <= 'L':
            
                numeric_phone += '5'
            
            elif 'M' <= character <= 'O':
            
                numeric_phone += '6'
            
            elif 'P' <= character <= 'R':
            
                numeric_phone += '7'
            
            elif 'T' <= character <= 'U':
            
                numeric_phone += '8'
            
            elif 'W' <= character <= 'Z':
            
                numeric_phone += '9'
        
        # If the character is not a letter, add it to the numeric phone number as is.
        else:
        
            numeric_phone += character

    # Return the translated numeric phone number.
    return numeric_phone

# Call the main function.
main()
