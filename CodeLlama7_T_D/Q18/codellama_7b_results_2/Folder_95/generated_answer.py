
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 57
    end_index = 84

    # Iterate through the list in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current index is divisible by either -30 or -88
        if my_list[i] % (-30) == 0 or my_list[i] % (-88) == 0:
            # If it is, add it to the total
            total += my_list[i]

    # Return the total
    return total
