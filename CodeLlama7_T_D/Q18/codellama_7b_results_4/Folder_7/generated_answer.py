
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the sum and the range of indices
    total = 0
    start_index = 543
    end_index = 584
    # Iterate over the list within the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current integer is divisible by either -553 or -737
        if my_list[i] % (-553) == 0 or my_list[i] % (-737) == 0:
            # If it is, add it to the sum
            total += my_list[i]
    # Return the sum of all divisible integers within the specified range
    return total
