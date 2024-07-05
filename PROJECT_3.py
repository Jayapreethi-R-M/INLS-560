__author__ = 'Jayapreethi Radhakrishnan Madanraj, jayam@ad.unc.edu, Onyen = jayam'

# Asking the user to enter their selection between one number and a range
single_or_range = input("Enter 'single' or 'range' to solve for a single square root or a range of values, respectively: ")

# Assuring the number is more than 0
if single_or_range == "single":
    user_value = int(input("Enter a positive integer value: "))
    while user_value <= 0:
        print("Your value is not above 0.")
        user_value = int(input("Please re-enter a positive integer value above 0: "))

    # Calculating the square root for the given number.
    final_value = 1
    estimate_value = user_value
    epsilon = 0.0001
    print("{:>5} {:>15}".format("Value", "Square Root"))
    while estimate_value - final_value > epsilon:
        estimate_value = (estimate_value + final_value) / 2
        final_value = user_value / estimate_value
    print("{:>5} {:>15.3f}".format(user_value, final_value))

# Calculating square root of numbers in the range as given by the user.
elif single_or_range == "range":
    start_num = int(input("Enter a positive integer value to start your range: "))
    end_num = int(input("Enter a positive integer value to end your range: "))

    while start_num <= 0 or end_num <= 0 or start_num >= end_num:
        print("Please re-enter a positive integer value above 0 and make sure that the start value must be lesser than the end value:")
        start_num = int(input("Enter a positive integer value to start your range: "))
        end_num = int(input("Enter a positive integer value to end your range: "))

    print("{:<10} {:>15}".format("Value", "Square root"))
    for num in range(start_num, end_num + 1):
        final_value = 1
        estimate_value = num
        epsilon = 0.0001
        while estimate_value - final_value > epsilon:
            estimate_value = (estimate_value + final_value) / 2
            final_value = num / estimate_value
        print("{:>5} {:>20.3f}".format(num, final_value))

else:
    print("Please enter 'single' or 'range' for the calculation mode.")
