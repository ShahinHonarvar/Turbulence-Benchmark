
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 306
    end_index = 957
    # Iterate through the list from the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current integer is divisible by either 982 or 319
        if my_list[i] % 982 == 0 or my_list[i] % 319 == 0:
            # Add the current integer to the sum
            sum += my_list[i]
    return sum
