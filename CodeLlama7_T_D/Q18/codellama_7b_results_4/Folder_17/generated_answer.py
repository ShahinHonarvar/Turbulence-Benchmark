
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 81
    end_index = 89
    total = 0

    # Loop through the specified range and calculate the sum of all integers divisible by either 56 or 68
    for i in range(start_index, end_index + 1):
        if my_list[i] % 56 == 0 or my_list[i] % 68 == 0:
            total += my_list[i]

    # Return the sum of all integers divisible by either 56 or 68 from index 81 to index 89, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
