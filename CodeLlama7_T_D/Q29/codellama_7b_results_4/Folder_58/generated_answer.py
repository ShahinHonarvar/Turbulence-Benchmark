
def gcf_two_nums(my_list):
    # Get the two numbers from the list
    num1 = my_list[129]
    num2 = my_list[582]
    # Initialize the greatest common factor to 1
    gcf = 1
    # Loop through the factors of both numbers
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            # If the factor is common to both numbers, update the gcf
            gcf = i

    return gcf
