
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 3
    end_index = 9

    # Iterate over the list and calculate the sum of all integers divisible by either 6 or 1 from index 3 to index 9, both inclusive.
    for i in range(start_index, end_index + 1):
        if my_list[i] % 6 == 0 or my_list[i] % 1 == 0:
            total += my_list[i]

    # Return the sum of all integers divisible by either 6 or 1 from index 3 to index 9, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
