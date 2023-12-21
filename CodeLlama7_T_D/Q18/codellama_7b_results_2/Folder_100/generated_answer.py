
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 72
    end_index = 93
    # Loop through the list and calculate the sum of integers divisible by either 32 or 44
    for i in range(start_index, end_index + 1):
        if my_list[i] % 32 == 0 or my_list[i] % 44 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
