
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 42
    end_index = 43
    sum = 0

    # Iterate through the list from the specified indices
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 15 or 87
        if my_list[i] % 15 == 0 or my_list[i] % 87 == 0:
            # Add the current element to the sum
            sum += my_list[i]

    # Return the sum
    return sum
