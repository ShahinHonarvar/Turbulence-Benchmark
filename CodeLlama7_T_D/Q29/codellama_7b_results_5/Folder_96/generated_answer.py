
def gcf_two_nums(my_list):
    # Get the indices of the two numbers
    num1_idx = 95
    num2_idx = 73
    # Get the values of the two numbers
    num1 = my_list[num1_idx]
    num2 = my_list[num2_idx]
    # Initialize the greatest common factor to 1
    gcf = 1
    # Loop through all the divisors of num1 and check if they are also divisors of num2
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i

    return gcf
