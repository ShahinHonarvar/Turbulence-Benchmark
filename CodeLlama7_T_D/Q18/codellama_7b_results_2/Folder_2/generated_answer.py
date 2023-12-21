
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the range of indices
    total = 0
    start = 73
    end = 86
    # Iterate over the specified range of indices in the list
    for i in range(start, end + 1):
        # Check if the current element is divisible by either 54 or 82
        if my_list[i] % 54 == 0 or my_list[i] % 82 == 0:
            # If it is, add it to the total sum
            total += my_list[i]
    # Return the total sum of all integers divisible by either 54 or 82 from index 73 to index 86, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
