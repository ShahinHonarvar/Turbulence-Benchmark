 def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 48
    end_index = 76
    sum = 0

    # Iterate over the list within the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either -46 or -82
        if my_list[i] % -46 == 0 or my_list[i] % -82 == 0:
            # Add the current element to the sum
            sum += my_list[i]

    # Return the sum of all integers divisible by either -46 or -82 within the specified range
    return sum
