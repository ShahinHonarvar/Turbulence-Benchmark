
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 61
    end_index = 88
    sum = 0

    # Loop through the list and add up the divisible integers
    for i in range(start_index, end_index + 1):
        if my_list[i] % 31 == 0 or my_list[i] % 11 == 0:
            sum += my_list[i]

    # Return the sum of the divisible integers
    return sum
