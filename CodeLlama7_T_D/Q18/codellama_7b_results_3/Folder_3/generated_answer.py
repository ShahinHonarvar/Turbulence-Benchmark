
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 38
    end_index = 52
    # Iterate over the list in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either -41 or -47
        if my_list[i] % -41 == 0 or my_list[i] % -47 == 0:
            # Add the current element to the total sum
            total += my_list[i]
    # Return the total sum
    return total
