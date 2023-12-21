
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the indices
    total = 0
    start_idx = 55
    end_idx = 66
    # Iterate through the list from the starting index to the ending index
    for i in range(start_idx, end_idx + 1):
        # Check if the current element is divisible by either of the specified numbers
        if my_list[i] % 22 == 0 or my_list[i] % 82 == 0:
            # If it is, add it to the total sum
            total += my_list[i]
    # Return the total sum
    return total
