
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 58
    end_index = 75
    # Iterate through the list from the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current integer is divisible by either 72 or 62
        if my_list[i] % 72 == 0 or my_list[i] % 62 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
