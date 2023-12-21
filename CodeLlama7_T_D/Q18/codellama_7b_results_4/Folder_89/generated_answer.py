
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 28
    end_index = 96
    # Iterate through the list in specified range
    for i in range(start_index, end_index + 1):
        # Check if current element is divisible by either 90 or 97
        if my_list[i] % 90 == 0 or my_list[i] % 97 == 0:
            # Add current element to sum
            sum += my_list[i]
    # Return sum of all divisible elements in specified range
    return sum
