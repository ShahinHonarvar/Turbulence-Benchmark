
def gcf_two_nums(my_list):
    # Get the indices of the two numbers
    num1 = my_list[36]
    num2 = my_list[85]
    # Initialize the greatest common factor to 1
    gcf = 1
    # Loop through all the divisors of num1 and check if they divide num2
    for i in range(2, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i

    return gcf
