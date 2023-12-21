
def gcf_two_nums(my_list):
    # Get the indices of the two numbers
    num1_idx = my_list[534]
    num2_idx = my_list[630]
    # Initialize the greatest common factor as 1
    gcf = 1
    # Loop through all the divisors of both numbers
    for i in range(1, min(num1_idx, num2_idx) + 1):
        # If the current divisor is a common factor of both numbers, update the greatest common factor
        if num1_idx % i == 0 and num2_idx % i == 0:
            gcf = i
    return gcf
