import math


# After I had read the given scenario, I began my work by defining the two 
# functions required for this project. The below function is the "investment_calculator."

def investment_calculator():

    # here the user is asked to input relevant values for investment calculation

    P = float(input("Enter the amount of money that you are depositing: "))
    r = float(input("Enter the interest rate (as a percentage): ")) / 100
    t = int(input("Enter the number of years you plan on investing: "))
    interest = input("Do you want 'simple' or 'compound' interest? ").lower()

    # Using the conditional statements we determine the total amount after interest using 
    # formulas given in the scenarion for the two types of interest: "simple" or "compound"

    if interest == "simple":
        A = P * (1 + r * t)
    elif interest == "compound":
        A = P * math.pow((1 + r), t)
    else:
        print("Invalid input. Please enter 'simple' or 'compound' for interest.")
        return

    # The results will be printed here after the calculations and the correct formulas
    # used depending on the investor's choice.

    print(f"The total amount after {t} years at an interest rate of {r*100}% is: {A:.2f}")

# Here, I defined the 2nd function named bond_calculator using the values and formulas given.

def bond_calculator():
    # Get user input for bond calculation
    P = float(input("Enter the present value of the house: "))
    i = float(input("Enter the annual interest rate: ")) / 100 / 12
    n = int(input("Enter the number of months to repay the bond: "))

    # Calculate the monthly repayment amount using the Python equivalent formulas

    Repayment = (i * P) / (1 - math.pow((1 + i), -n))

    # This line prints the result of the bond calculation, 
    # formatted to ".2" decimals to display the monthly repayment amount.

    print(f"The monthly repayment amount for the bond is: {Repayment:.2f}")

# This line defines the main function, which serves as the entry point for the program.

def main():
# These lines display a welcome message and the menu options for the 
# user to choose between investment and bond calculations.
    print("Welcome to the Finance Calculator!")
    investment = "Investment - to calculate the interest you'll earn on your investment"
    print(investment)
    bond = "Bond       - to calculate the amount you'll have to pay on a home loan"
    print(bond)
    print("Please choose the calculation you want to perform:")
    print("1. Investment")
    print("2. Bond")

# This line prompts the user to enter their choice and converts 
# the input to lowercase for case-insensitivity.

    choice = input("Enter 'investment' or 'bond': ").lower()

# These lines call the appropriate calculator function based on the user's choice.
# If the user enters an invalid choice, an error message is displayed

    if choice == "investment":
        investment_calculator()
    elif choice == "bond":
        bond_calculator()
    else:
        print("Invalid input. Please enter 'investment' or 'bond'.")

# This line ensures that the main() function is called when the script is executed

if __name__ == "__main__":
    main()