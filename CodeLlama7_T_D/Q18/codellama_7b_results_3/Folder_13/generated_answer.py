
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 13
    end_index = 18
    # Loop through the list and add up the divisible integers
    for i in range(start_index, end_index + 1):
        if my_list[i] % 45 == 0 or my_list[i] % 20 == 0:
            sum += my_list[i]
    # Return the sum of the divisible integers
    return sum
