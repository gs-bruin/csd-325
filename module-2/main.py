# This program uses a while loop to determine how long it takes 
# for an investment to double at a given interest rate.

# define calculate_investment as a function so that we can rerun the program 
# with a while loop

def calculate_investment():
    
    # Get the user's input for annualized interest rate
    interest_rate = float(input("Enter the annualized interest rate as a whole number. For example, enter 3 for 3%: "))

    # Print to confirm the interest rate
    print(f"The annualized interest rate is {interest_rate}%\n")

    # Get the user's input for initial investment (principal) and create variable
    principal = float(input("Enter the initial investment as a whole number: "))

    # Print to confirm the initial investment
    print(f"The initial investment is ${principal}\n")

    # Set the initial value of the number of years
    years_of_investment = 0

    # Confirm all details with the user, output details of calculation back to the user
    # State the program's goal using the user's input

    # Convert the interest rate to a decimal
    decimal_interest_rate = interest_rate / 100

    # Calculate the investment accrued
    investment_accrued = principal

    # Use a while loop to compound interest until the principal doubles
    while investment_accrued < principal * 2:
        investment_accrued = investment_accrued + (investment_accrued * decimal_interest_rate)
        years_of_investment = years_of_investment + 1
        print(f"Year {years_of_investment}: Investment accrued is ${investment_accrued}.")  

    # Output the result
    print(f"\nIt takes {years_of_investment} years for the investment to double. The final investment accrued is ${investment_accrued}.\n")
    
    # Prompt user to choose to rerun or exit
    choice = input("Enter 'r' to rerun or any other key to exit: ")
    print("\n\n\n")
    return choice.lower() == 'r'


# Use a while loop to continuously run the program until the user chooses to exit

# create an infinite loop until break statement is reached
while True:
    # checks if calculate_investment returns False
    if not calculate_investment():
        # if False, break out of the loop
        break

# calculate_investment returns True if the user inputs 'r', so the program will rerun
        
# if the user inputs anything other than 'r', the program exits
# due to the break statement intitated when calculate_investment returns False