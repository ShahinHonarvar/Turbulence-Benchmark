
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 31
    end_index = 50
    # Iterate through the list from the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 81 or 64
        if my_list[i] % 81 == 0 or my_list[i] % 64 == 0:
            # If it is, add it to the total
            total += my_list[i]
    # Return the sum of all divisible integers
    return total
