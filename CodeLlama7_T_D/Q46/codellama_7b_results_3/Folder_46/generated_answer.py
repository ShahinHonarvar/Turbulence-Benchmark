
def gcf_three_nums(my_list):
    # Get the elements at indices 78, 19 and 13
    num1 = my_list[78]
    num2 = my_list[19]
    num3 = my_list[13]
    # Initialize the greatest common factor to 1
    gcf = 1
    # Check if any of the numbers are not equal to 1
    if num1 != 1 or num2 != 1 or num3 != 1:
        # Loop through all the possible factors of num1
        for i in range(2, num1 + 1):
            # If the current factor is a divisor of all three numbers
            if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
                # Update the greatest common factor
                gcf = i
                break

    return gcf
