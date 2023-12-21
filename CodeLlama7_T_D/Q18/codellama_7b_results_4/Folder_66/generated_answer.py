
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 58
    end_index = 81
    # Iterate through the list from the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current index is divisible by either 55 or 10
        if my_list[i] % 55 == 0 or my_list[i] % 10 == 0:
            # Add the current element to the sum
            sum += my_list[i]
    return sum
