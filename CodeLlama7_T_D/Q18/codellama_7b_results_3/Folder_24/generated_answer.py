 def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 29
    end_index = 53
    # Loop through the list, starting from the specified index
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either -68 or -85
        if my_list[i] % (-68) == 0 or my_list[i] % (-85) == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
