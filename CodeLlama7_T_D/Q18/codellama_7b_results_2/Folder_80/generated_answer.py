 def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 14
    end_index = 93
    # Iterate through the list in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current integer is divisible by either 71 or 81
        if my_list[i] % 71 == 0 or my_list[i] % 81 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
