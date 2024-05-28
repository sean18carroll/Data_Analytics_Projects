# Seán Carroll
# Assignment Question 2 Part A
# DBS amateur Golf Club has a tournament every weekend. The club president has asked you to write 2 programs.
# 1. A program that will read each player's name and golf score as keyboard input, then save these to a file named golf.txt. 
# Each record will have a field for the player's name and a field for the player's score.

# Define the main function
def main():

    # Get the number of players playing in the tournament
    players_played = int(input('Enter the number of players in the Tournament: '))

    # Open file for writing and call it golf_file
    golf_file = open(r'/Users/seancarroll/Desktop/Programming for Data Analytics/Python Programs/Assignment Questions/Assignment_Question2/golf.txt', 'w')

    # Using the number of players entered use a for loop to find the following details for the competition.
    for count in range(1, players_played +1):

        # Find the player's first name. The str(count) is used to desplay the player's corresponding number.
        first_name = input("Enter the first name of golfer #" + str(count) + ': ') 

        # Find the player's last name.
        last_name = input("Enter the last name of golfer #" + str(count) + ': ')

        # Find the player's golf handicap.
        handicap = int(input("Enter the handicap of golfer #" + str(count) + ': '))

        # Find the player's score after the first 9 holes.
        front9score = int(input("Enter the score thru the front 9 of golfer #" + str(count) + ': '))

        # Find the player's score after the last 9 holes.
        back9score = int(input("Enter the score thru the back 9 of golfer #" + str(count) + ': '))

        # Formula to calculate the golfer's total score
        totalscore = front9score + back9score

        # Display the player's total score.
        print(totalscore, ' is the total score (before handicap considered) of golfer #', str(count), sep='')

        # Formula to calculate the player's score after handicap is taken into consideration.
        score_after_handicap = totalscore - handicap

        # Display the player's score after handicap is taken into consideration.
        print(score_after_handicap, ' is the score (after handicap considered) of golfer #', str(count), sep='')

        print('')

        # Write the data into the golf.txt file. Use '\n' to write the data onto the new line.
        golf_file.write(str(first_name) + '\n')
        
        golf_file.write(str(last_name) + '\n')

        golf_file.write(str(handicap) + '\n')
        
        golf_file.write(str(front9score) + '\n')

        golf_file.write(str(back9score) + '\n')
        
        golf_file.write(str(totalscore) + '\n')

        golf_file.write(str(score_after_handicap) + '\n')
    
    # Close the golf_file file
    golf_file.close()
    print('Data is written to this file.')

# Call he main function
main()