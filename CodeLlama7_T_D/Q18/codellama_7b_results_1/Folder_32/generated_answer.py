
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the sum and the range of indices
    sum = 0
    start_index = 25
    end_index = 95
    # Iterate over the specified range of indices
    for i in range(start_index, end_index + 1):
        # If the current index is divisible by either 51 or 77, add it to the sum
        if my_list[i] % 51 == 0 or my_list[i] % 77 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either 51 or 77 from index 25 to index 95, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
