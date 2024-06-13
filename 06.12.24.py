# This script demonstrates basic Python concepts and constructs

# Assigning a string value to a variable
name = "Sam"

# The following lines are commented out code snippets showcasing various functionalities

##print(name)  # Print the value of the variable 'name'

##for i in range(3):  # Loop to print 'name' three times
##    print(name)
    
##for i in range(1, 5):  # Loop to print numbers from 1 to 4
##    print(i)

##l_5 = list(range(5))  # Create a list of numbers from 0 to 4

####for i in range(2, 12, 2):  # Loop to print even numbers from 2 to 10
####    print(i)
##for num in l_5:  # Loop to print each number in the list l_5
##    print(num)

##def hello(name):  # Function to greet a user by their name
##    name = input("Enter name:")  # Get user input
##    print("Hello " + name)  # Print a greeting message

##hello("Sam")  # Call the hello function with "Sam" as an argument

##def blank():  # Function to print a blank line
##    print()

##def blank_3():  # Function to print three blank lines
##    blank()
##    blank()
##    blank()

##numbers = [1, 5, 2, 4, 6, 10, 3]  # List of numbers

##for number in numbers:  # Loop to check if each number is even or odd
##    if number % 2 == 0:
##        print(number, "is even")
##    else:
##        print(number, "is odd")

##numbers = [1, -5, 2, -4, 0, 6, -10, 3]  # List of positive, negative, and zero numbers

##for number in numbers:  # Loop to check if each number is positive, negative, or zero
##    if number == 0:
##        print("Zero")
##    elif number > 0:
##        print("positive")
##    else:
##        print("negative")

##def even(x):  # Function to check if a number is even
##    if x % 2 == 0:
##        return True

# Nested loops to print a grid pattern
for row in range(5):  # Outer loop for rows
    #print(row)  # Print the current row number
    for col in range(5):  # Inner loop for columns
        print(col, end=' ')  # Print the column number with a space
    print()  # Print a newline after each row
