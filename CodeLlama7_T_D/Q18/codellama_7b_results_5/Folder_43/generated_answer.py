
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 57
    end_index = 85
    # Loop through the list and add up the divisible integers
    for i in range(start_index, end_index + 1):
        if my_list[i] % -77 == 0 or my_list[i] % -32 == 0:
            total += my_list[i]
    # Return the sum of the divisible integers
    return total
