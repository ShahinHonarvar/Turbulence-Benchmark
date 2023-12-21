
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for sum and indices
    sum = 0
    start_idx = 13
    end_idx = 91
    # Loop through the list from start to end index
    for i in range(start_idx, end_idx + 1):
        # If the current integer is divisible by either -65 or -62
        if my_list[i] % (-65 or -62) == 0:
            # Add the current integer to the sum
            sum += my_list[i]
    return sum
