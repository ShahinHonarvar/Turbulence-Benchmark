
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 6
    end_index = 9

    # Iterate over the list and calculate the sum of integers divisible by either -1 or -10
    for i in range(start_index, end_index + 1):
        if my_list[i] % -1 == 0 or my_list[i] % -10 == 0:
            total += my_list[i]

    # Return the sum
    return total
