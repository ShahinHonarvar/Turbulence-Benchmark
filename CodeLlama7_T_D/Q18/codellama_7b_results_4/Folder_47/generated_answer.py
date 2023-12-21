
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 42
    end_index = 87
    # Loop through the list and calculate the sum of all integers divisible by either -90 or -74
    for i in range(start_index, end_index + 1):
        if my_list[i] % -90 == 0 or my_list[i] % -74 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
