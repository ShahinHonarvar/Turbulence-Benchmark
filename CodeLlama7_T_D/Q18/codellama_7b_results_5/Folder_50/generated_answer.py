
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 46
    end_index = 91

    # Iterate over the list and add up the divisible integers
    for i in range(start_index, end_index + 1):
        if my_list[i] % 67 == 0 or my_list[i] % 15 == 0:
            total += my_list[i]

    # Return the sum of all divisible integers
    return total
