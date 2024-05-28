# Seán Carroll
# Assignment Question 3 Part A
# Create a Text File that contains your expenses for the last month in the following categories:
#  Rent, Gas, Food, clothing, Car Payments, Misc

# Define the main function.
def main():

    # Open a file called expenses_file to be written.
    expenses_file = open(r'/Users/seancarroll/Desktop/Programming for Data Analytics/Python Programs/Assignment Questions/Assignment_Question3/Expenses.txt', 'w')

    # Ask the user for their total expenditure on rent for the last month.
    rent = int(input("Rent expenditure last month: €" ))

    # Ask the user for their total expenditure on gas for the last month.
    gas = int(input("Gas expenditure last month: €"))

    # Ask the user for their total expenditure on food for the last month.
    food = int(input("Food expenditure last month: €"))

    # Ask the user for their total expenditure on clothing for the last month.
    clothing = int(input("Clothing expenditure last month: €"))

    # Ask the user for their total expenditure on car payments for the last month.
    car_payments = int(input("Car payments last month: €"))

    # Ask the user for their total expenditure on misc for the last month.
    misc = int(input("Misc expenditure last month: €"))

    
    # Write the expenditure from the user into the expenses_file file. Use '\n' to write the data onto a new line.
    expenses_file.write(str('Rent') + '\n')
    
    expenses_file.write(str(rent) + '\n')

    expenses_file.write(str('Gas') + '\n')

    expenses_file.write(str(gas) + '\n')

    expenses_file.write(str('Food') + '\n')

    expenses_file.write(str(food) + '\n')

    expenses_file.write(str('Clothing') + '\n')

    expenses_file.write(str(clothing) + '\n')

    expenses_file.write(str('Car') + '\n')

    expenses_file.write(str(car_payments) + '\n')

    expenses_file.write(str('Misc') + '\n')

    expenses_file.write(str(misc))

    # Close the file.
    expenses_file.close()

# Call the main function.
main()