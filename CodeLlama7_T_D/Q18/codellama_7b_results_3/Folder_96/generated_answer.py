
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    i = 50
    # Loop through the list, starting from index 50
    while i <= 200:
        # If the current element is divisible by either -34 or 64
        if my_list[i] % (-34) == 0 or my_list[i] % (64) == 0:
            # Add it to the sum
            sum += my_list[i]
        i += 1

    # Return the sum
    return sum
