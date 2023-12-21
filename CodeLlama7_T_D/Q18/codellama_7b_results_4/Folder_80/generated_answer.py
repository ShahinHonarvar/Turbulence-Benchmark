
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 14
    end_index = 93

    # Iterate through list and add up divisible values
    for i in range(start_index, end_index + 1):
        if my_list[i] % 71 == 0 or my_list[i] % 81 == 0:
            total += my_list[i]

    # Return sum of divisible values
    return total
