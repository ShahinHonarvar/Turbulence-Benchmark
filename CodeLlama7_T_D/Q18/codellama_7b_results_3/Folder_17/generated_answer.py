
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for tracking the sum and the range of indices to consider
    sum = 0
    start_index = 81
    end_index = 89
    # Iterate over the list, starting at the specified index and ending at the specified index
    for i in range(start_index, end_index + 1):
        # If the current element is divisible by either 56 or 68, add it to the sum
        if my_list[i] % 56 == 0 or my_list[i] % 68 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either 56 or 68 from index 81 to index 89, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
