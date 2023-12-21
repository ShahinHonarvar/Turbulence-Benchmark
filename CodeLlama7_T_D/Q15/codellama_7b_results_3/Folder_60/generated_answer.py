
def sum_odd_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 75
    end_index = 85
    # Iterate over the list from the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current index is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current index to the sum
            sum += my_list[i]
    # Return the sum of all odd integers from the specified range
    return sum
