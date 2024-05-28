# Seán Carroll
# Assignment Question 2 Part B
# 2. A  program that reads the record from the golf.txt file and displays them.

# Define the main function.
def main():

    # Open the golf_file so that it can be read.
    golf_file = open(r'/Users/seancarroll/Desktop/Programming for Data Analytics/Python Programs/Assignment Questions/Assignment_Question2/golf.txt', 'r')

    # Read the first line from the file which is the first name.
    first_name = golf_file.readline()

    # While first_name is not at the end of the file [EOF].
    while first_name!= '':

        # Read the last name.
        last_name = golf_file.readline()

        # Read the handicap.
        handicap = golf_file.readline()

        # Read the score for the front 9 holes.
        front9score = golf_file.readline()

        # Read the score for the back 9 holes.
        back9score = golf_file.readline()
        
        # Read the total score for the round before the handicap is considered.
        totalscore = golf_file.readline()

        # Read the total score for the round after the handicap has been considered.
        score_after_handicap = golf_file.readline()


        # Use the .rstrip function to strip the new lines from the fields.
        first_name = first_name.rstrip('\n')

        last_name = last_name.rstrip('\n')

        handicap = handicap.rstrip('\n')

        front9score = front9score.rstrip('\n')

        back9score = back9score.rstrip('\n')

        totalscore = totalscore.rstrip('\n')

        score_after_handicap = score_after_handicap.rstrip('\n')

        # Display the records.
        print('First Name:', first_name)

        print('Last Name:', last_name)

        print('Handicap:', handicap)

        print('Front 9 Score:', front9score)

        print('Back 9 Score:', back9score)
        
        print('Total Score (Before Handicap):', totalscore)

        print('Total Score (After Handicap):', score_after_handicap)

        print('')

        # Read the name field for the next record. 
        # As the last line is blank the program will finish the loop when the code meets this blank line.
        first_name = golf_file.readline()

    # Close the file.
    golf_file.close()

# Call the main function.
main()