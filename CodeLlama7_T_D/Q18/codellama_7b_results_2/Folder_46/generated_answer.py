
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 11
    end_index = 46
    # Iterate through the list from start to end index
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 55 or 36
        if my_list[i] % 55 == 0 or my_list[i] % 36 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
