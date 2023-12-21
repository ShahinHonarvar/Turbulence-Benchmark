
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 81
    end_index = 86
    # Iterate through the list and add up the integers divisible by either -33 or -62
    for i in range(start_index, end_index + 1):
        if my_list[i] % (-33) == 0 or my_list[i] % (-62) == 0:
            sum += my_list[i]
    # Return the sum
    return sum
