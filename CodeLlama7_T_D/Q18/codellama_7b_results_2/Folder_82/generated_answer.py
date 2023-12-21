 def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 20
    end_index = 200
    # Iterate through the list in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either -20 or -200
        if my_list[i] % -20 == 0 or my_list[i] % -200 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
