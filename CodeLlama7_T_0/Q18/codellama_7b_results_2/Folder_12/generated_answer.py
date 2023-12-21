
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 35
    end_index = 64
    # Iterate through the list and calculate the sum of all integers divisible by either -30 or -95
    for i in range(start_index, end_index + 1):
        if my_list[i] % -30 == 0 or my_list[i] % -95 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
