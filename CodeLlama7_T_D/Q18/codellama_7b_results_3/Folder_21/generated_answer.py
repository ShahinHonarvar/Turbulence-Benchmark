
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the range of indices to consider
    start_index = 315
    end_index = 934
    # Initialize the sum variable to 0
    sum = 0
    # Iterate over the specified range of indices
    for i in range(start_index, end_index + 1):
        # If the current element is divisible by either -897 or -556, add it to the sum
        if my_list[i] % -897 == 0 or my_list[i] % -556 == 0:
            sum += my_list[i]
    # Return the final sum
    return sum
