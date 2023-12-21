
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 55
    end_index = 66
    sum = 0

    # Iterate through the list, starting from the specified index
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 22 or 82
        if my_list[i] % 22 == 0 or my_list[i] % 82 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
