
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 93
    end_index = 94

    # Loop through the list, starting from the specified index and ending at the specified index
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either -53 or -91
        if my_list[i] % -53 == 0 or my_list[i] % -91 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
