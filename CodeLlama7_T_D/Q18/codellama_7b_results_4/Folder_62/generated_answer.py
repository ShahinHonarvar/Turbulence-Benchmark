
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 44
    end_index = 59
    # Loop through the list and add up all integers divisible by either 39 or 15
    for i in range(start_index, end_index + 1):
        if my_list[i] % 39 == 0 or my_list[i] % 15 == 0:
            total += my_list[i]
    # Return the sum of all integers divisible by either 39 or 15 from index 44 to index 59, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
