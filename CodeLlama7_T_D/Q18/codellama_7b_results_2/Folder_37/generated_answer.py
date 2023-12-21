
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 2
    end_index = 7

    # Iterate through the list and calculate the sum of all integers divisible by either -1 or -7
    for i in range(start_index, end_index + 1):
        if my_list[i] % (-1) == 0 or my_list[i] % (-7) == 0:
            total += my_list[i]

    # Return the sum of all integers divisible by either -1 or -7 from index 2 to index 7, both inclusive
    return total
