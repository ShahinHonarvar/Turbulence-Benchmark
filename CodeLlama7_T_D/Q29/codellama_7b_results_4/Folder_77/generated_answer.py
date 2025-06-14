
def gcf_two_nums(my_list):
    # Get the indices of the two numbers
    idx1 = my_list[841]
    idx2 = my_list[804]
    # Initialize the greatest common factor to 1
    gcf = 1
    # Iterate through the factors of the first number
    for i in range(idx1, 1, -1):
        # If the current factor is a divisor of both numbers, update the greatest common factor
        if idx1 % i == 0 and idx2 % i == 0:
            gcf = i

    return gcf
