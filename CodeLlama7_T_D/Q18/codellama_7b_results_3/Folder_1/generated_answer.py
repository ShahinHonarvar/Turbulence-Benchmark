
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 10
    end_index = 28
    # Loop through the list and add up the divisible integers
    for i in range(start_index, end_index + 1):
        if my_list[i] % -61 == 0 or my_list[i] % -64 == 0:
            total += my_list[i]
    # Return the sum of the divisible integers
    return total
