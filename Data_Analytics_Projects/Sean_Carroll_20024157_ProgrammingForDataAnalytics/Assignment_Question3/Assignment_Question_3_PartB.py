# Seán Carroll
# Assignment Question 3 Part B
# Write a python program that reads the Data from the file and uses matplotlib to plot a pie chart showing how you spent your money.

# Import the required module, matplotlib.pyplot
import matplotlib.pyplot as plt

# Define the main module
def main():

    # Declare the expenses_file and open it so that it can be read
    expenses_file = open(r'/Users/seancarroll/Desktop/Programming for Data Analytics/Python Programs/Assignment Questions/Assignment_Question3/Expenses.txt', 'r')

    # Create empty lists for categories and amounts
    categories_list = []

    amounts_list = []

    # Read all lines from the file
    lines = expenses_file.readlines()

    # Using a for loop from 0 up to the number of lines in iterations of 2.
    for i in range(0, len(lines), 2):
        
        # Extract categories from current line. Call it categories.
        categories = lines[i]
        
        # Extract amounts from the next line, and convert to an integer. Call it amounts.
        amounts = int(lines[i + 1])

        # Append categories_list and amounts_list to their respective lists
        categories_list.append(categories)
        
        amounts_list.append(amounts)

    # Go to the function pie_chart. Bring the amounts list and the categories list that was created.
    pie_chart(amounts_list, categories_list)

    # Go to the function bar_chart. Bring the amounts list and the categories list that was created.
    bar_chart(amounts_list, categories_list)

    # Go to the function line_graph. Bring the amounts list and the categories list that was created.
    line_graph(amounts_list, categories_list)

    # Close the expenses_file file.
    expenses_file.close()
        

# Define the pie_chart function. The amounts_list and the categories_list have been brought from the main function.
def pie_chart(amounts_list, categories_list):

    # Create a pie chart.
    plt.pie(amounts_list, labels=categories_list, autopct='%1.2f%%')
        
    # Add a title.
    plt.title('Monthly Expenses')
        
    # Show the pie chart.
    plt.show()


# Define the bar_chart function. The amounts_list and the categories_list have been brought from the main function.
def bar_chart(amounts_list, categories_list):

    # Create a list with x coordinates of each bar's left edge. 
    # For each index i in the range of indices, it calculates i * 10 and adds the result to the list.
    left_edge = [i * 10 for i in range(len(amounts_list))]

    # Create a variable for bar width
    bar_width = 10

    # Build the bar chart
    plt.bar(left_edge, amounts_list, bar_width, color=('r','g','b','y','k','c'))

    # Add a title
    plt.title('Monthly Expenses')

    # Add labels to the axes
    plt.xlabel('Category')

    plt.ylabel('Amount')

    # Customise the tick marks
    plt.xticks([i * 10 for i in range(len(amounts_list))], 
               categories_list)

    plt.yticks([0,100,200,300,400,500,600,700],
              ['€0', '€100', '€200', '€300', '€400', '€500', '€600', '€700'])
    
    # Display the bar chart
    plt.show()


# Define the line_graph function. The amounts_list and the categories_list have been brought from the main function.
def line_graph(amounts_list, categories_list):

    # Build the line graph
    plt.plot(categories_list, amounts_list)

    # Add a title
    plt.title('Monthly Expenses')

    # Add labels to the axes
    plt.xlabel('Categories')
    plt.ylabel('Amounts')

    # Set the axes limits
    plt.xlim(xmin = -1, xmax = 6)
    plt.ylim(ymin = -1, ymax = 700)

    # Add a grid
    plt.grid(True)
    
    # Display
    plt.show()


# Return to the main function.
main()
