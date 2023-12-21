
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 68
    end_index = 99

    # Iterate through the list and add up the integers divisible by either -37 or -26
    for i in range(start_index, end_index + 1):
        if my_list[i] % (-37) == 0 or my_list[i] % (-26) == 0:
            total += my_list[i]

    # Return the sum of all integers divisible by either -37 or -26 from index 68 to index 99, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
