__author__ = 'Jayapreethi Radhakrishnan Madanraj, jayam@ad.unc.edu, Onyen = jayam'
print("Welcome to the Compound Interest Calculator.")

# Following are the code to input the initial set of values for final account balance calculator
initial_amt = int(input("Please enter the initial amount of your investment(in $): "))
int_rate = float(input("Please enter the interest rate (e.g., '.03' for 3% interest): "))
num_yrs = float(input("Please enter the number of years for the investment: "))
num_compound = int(input("Please enter the number of compoundings per year: "))
final_amt = initial_amt * ((1 + (int_rate / num_compound)) ** (num_compound * num_yrs))

# Code to display the results of the initial calculations
print("Original Investment:  $", "{:,.2f}".format(initial_amt))
print("Interest Earned:      $", "{:,.2f}".format(final_amt - initial_amt))
print("Final Balance:        $", "{:,.2f} \n ".format(final_amt) )

# Code to ask the user if they would like to continue or end the program5
cont = input("Would you like to compare this to another savings option? (Y/N) ")

if cont == 'Y':
    # Following are the code to input the second set of values for final account balance calculator
    initial_amt1 = int(input("Please enter the initial amount of your investment(in $): "))
    int_rate1 = float(input("Please enter the interest rate (e.g., '.03' for 3% interest): "))
    num_yrs1 = float(input("Please enter the number of years for the investment: "))
    num_compound1 = int(input("Please enter the number of compoundings per year: "))
    final_amt1 = initial_amt1 * ((1 + (int_rate1 / num_compound1)) ** (num_compound1 * num_yrs1))

    # Code to display the results of the second calculations
    print("Original Investment: $", "{:,.2f}".format(initial_amt1))
    print("Interest Earned:     $", "{:,.2f}".format(final_amt1 - initial_amt1))
    print("Final Balance:       $", "{:,.2f} \n".format(final_amt1))

    # If function to compare the final account balance
    if final_amt > final_amt1:
        print("The first option will result in the largest final account balance.")
    elif final_amt1 > final_amt:
        print("The second option will result in the largest final account balance.")
    else:
        print("The first and second option will result in same final account balance.")
else:
    print("Thanks for using the Compound Interest Calculator.")