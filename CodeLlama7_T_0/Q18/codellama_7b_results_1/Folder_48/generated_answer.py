
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 306
    end_index = 957
    # Iterate through the list and calculate the sum of all integers divisible by either 982 or 319
    for i in range(start_index, end_index + 1):
        if my_list[i] % 982 == 0 or my_list[i] % 319 == 0:
            total += my_list[i]
    # Return the sum of all integers divisible by either 982 or 319 from index 306 to index 957, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
