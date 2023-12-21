
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 51
    end_index = 76
    # Loop through the list from the specified indices
    for i in range(start_index, end_index + 1):
        # Check if the current integer is divisible by either -90 or -59
        if my_list[i] % (-90) == 0 or my_list[i] % (-59) == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
