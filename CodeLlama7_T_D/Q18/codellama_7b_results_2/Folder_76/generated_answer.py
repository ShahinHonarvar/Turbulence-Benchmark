
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 250
    end_index = 629
    # Loop through the list and calculate the sum of all integers divisible by either 850 or 587
    for i in range(start_index, end_index + 1):
        if my_list[i] % 850 == 0 or my_list[i] % 587 == 0:
            total += my_list[i]
    # Return the sum of all integers divisible by either 850 or 587 from index 250 to index 629, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
