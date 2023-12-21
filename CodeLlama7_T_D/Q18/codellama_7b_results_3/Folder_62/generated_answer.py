
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the range of indices and the sum
    start_index = 44
    end_index = 59
    sum = 0

    # Loop through the specified range of indices
    for i in range(start_index, end_index + 1):
        # Check if the current index is divisible by either 39 or 15
        if my_list[i] % 39 == 0 or my_list[i] % 15 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum of all integers divisible by either 39 or 15 from index 44 to index 59, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
