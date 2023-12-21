
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 81
    end_index = 89

    # Iterate over the list in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 56 or 68
        if my_list[i] % 56 == 0 or my_list[i] % 68 == 0:
            # If it is, add it to the total
            total += my_list[i]

    # Return the sum of all divisible integers in the specified range
    return total
