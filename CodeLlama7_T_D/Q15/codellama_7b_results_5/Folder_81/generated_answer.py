
def sum_odd_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 10
    end_index = 100
    # Iterate through the list from the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current index is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current value to the sum
            sum += my_list[i]
    # Return the sum of all odd integers from the specified range, or 0 if no odd integers exist in the range.
    return sum
