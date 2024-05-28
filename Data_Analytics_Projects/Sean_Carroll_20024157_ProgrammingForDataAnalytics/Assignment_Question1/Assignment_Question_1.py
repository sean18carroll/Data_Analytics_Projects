# Seán Carroll
# Assignment - Question 1
# A prime number is a number that is only divisible by itself and 1. E.G the number 5 is prime number because it can only be evenly divided by 1 and 5. 
# The number 6 is not a prime number because it can be divided by 1,2,3 and 6.
# Write a Boolean function named is_prime which takes an integer as an argument and returns true if the argument is a prime number, or false otherwise. 
# Use the function in a program that prompts the user to enter a number then display a message indicating whether the number is prime. 


# Define the main function
def main():

    # Ask the user to enter a number
    user_number = int(input('Enter a number: '))
    
    # Call the function is_prime and bring the number entered by the user to the is_prime function.
    # Assign the is_prime function to prime for when the result is returned to the main function.
    prime = is_prime(user_number)

    # The if statement assigns a print statement to a number if it returns True.
    if prime == True:
        
        # Print statement declares to the user that the number entered is a prime number.
        print('The number you entered is a prime number.')
        
    # Else statement assigns a print statement to a number that returns False.
    else:

        # Print statement declares to the user that the number entered is not a prime number.
        print('The number you entered is not a prime number.')
        
# The is_prime function will deduce whether or not the number entered by the user is a prime number or not
def is_prime(user_number):
    
    if user_number <= 1:
        return False  # 1 and negative numbers are not prime
    
    if user_number == 2:
        return True # 2 is a prime number
    
    # Iterate through numbers from 4 to (user_number - 1).
    for num in range(4, user_number):
        
        # Divide the user_number by all numbers from 4 up to the user_number-1. 
        # If there is no remainder then the number is not a prime number.
        # % gives the remainder (10 % 4 = 2)
        if user_number % num == 0:

            # Return False as the number is not a prime number.
            return False

    # The loop starts from i = 3 and iterates up to the square root of user_number (converted to an integer) with a step of 2. 
    # This is because any divisor of user_number greater than its square root will have a corresponding divisor smaller than the square root. 
    # The step of 2 ensures that only odd numbers are checked (since even numbers other than 2 cannot be prime).
    # Inside the loop, it checks if user_number is divisible evenly by i. 
    # If it is, the function immediately returns False, indicating that the number is not a prime number.
    # If the loop completes without finding any divisors, the function returns True, indicating that the number is a prime number.    
    for i in range(3, int(user_number**0.5) + 1, 2):
        
        if user_number % i == 0:
            
            # Found false as the number is not a prime number.
            return False

    # If not false and no divisors found, the number is prime    
    return True  

           
# Call on the main() function
main()

