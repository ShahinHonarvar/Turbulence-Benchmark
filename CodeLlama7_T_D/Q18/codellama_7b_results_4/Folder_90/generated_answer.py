
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the sum and the range of indices
    sum = 0
    start_idx = 138
    end_idx = 424
    # Iterate over the list in the specified range
    for i in range(start_idx, end_idx + 1):
        # Check if the current index is divisible by either -863 or -329
        if my_list[i] % -863 == 0 or my_list[i] % -329 == 0:
            # Add the current integer to the sum if it is divisible by either -863 or -329
            sum += my_list[i]
    # Return the sum of all integers divisible by either -863 or -329 in the specified range, or 0 if no such integers exist
    return sum
