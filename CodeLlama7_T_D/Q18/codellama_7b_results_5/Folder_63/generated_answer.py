
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 31
    end_index = 50
    # Iterate through the list and add up all integers divisible by either 81 or 64 from index 31 to index 50, both inclusive
    for i in range(start_index, end_index + 1):
        if my_list[i] % 81 == 0 or my_list[i] % 64 == 0:
            total += my_list[i]
    # Return the sum of all integers divisible by either 81 or 64 from index 31 to index 50, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
