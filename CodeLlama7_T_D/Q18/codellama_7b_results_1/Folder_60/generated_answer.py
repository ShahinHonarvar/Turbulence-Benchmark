
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the range of indices to consider
    total = 0
    start_index = 10
    end_index = 79
    # Iterate over the specified range of indices in the list
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either -74 or -58
        if my_list[i] % (-74) == 0 or my_list[i] % (-58) == 0:
            # If it is, add it to the sum
            total += my_list[i]
    # Return the sum of all integers divisible by either -74 or -58 from index 10 to index 79, both inclusive. If no such integers exist in the specified range, return 0.
    return total
