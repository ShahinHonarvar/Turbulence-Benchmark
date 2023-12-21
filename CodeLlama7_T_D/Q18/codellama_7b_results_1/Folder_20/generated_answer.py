
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 48
    end_index = 76
    # Loop through the list and calculate the sum of the divisible integers
    for i in range(start_index, end_index + 1):
        if my_list[i] % -46 == 0 or my_list[i] % -82 == 0:
            sum += my_list[i]
    # Return the sum of the divisible integers
    return sum
