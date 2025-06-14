
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 28
    end_index = 96
    # Iterate through the list and calculate the sum of all integers divisible by either 90 or 97 from index 28 to index 96, both inclusive
    for i in range(start_index, end_index + 1):
        if my_list[i] % 90 == 0 or my_list[i] % 97 == 0:
            total += my_list[i]
    # Return the sum of all integers divisible by either 90 or 97 from index 28 to index 96, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
