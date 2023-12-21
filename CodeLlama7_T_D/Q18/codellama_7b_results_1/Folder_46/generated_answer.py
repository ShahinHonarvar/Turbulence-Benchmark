
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the sum and the range of indices
    sum = 0
    start_index = 11
    end_index = 46
    # Iterate over the specified range of indices
    for i in range(start_index, end_index + 1):
        # Check if the current index is divisible by either 55 or 36
        if my_list[i] % 55 == 0 or my_list[i] % 36 == 0:
            # If it is, add its value to the sum
            sum += my_list[i]
    # Return the sum
    return sum
