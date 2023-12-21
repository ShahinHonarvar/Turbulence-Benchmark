
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 54
    end_index = 79

    # Iterate through the list in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 54 or 28
        if my_list[i] % 54 == 0 or my_list[i] % 28 == 0:
            # Add the current element to the total
            total += my_list[i]

    # Return the sum of all divisible integers in the specified range, or 0 if no such integers exist
    return total
