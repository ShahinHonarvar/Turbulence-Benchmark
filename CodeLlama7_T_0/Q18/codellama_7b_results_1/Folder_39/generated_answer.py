
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 13
    end_index = 76
    # Iterate through the list and calculate the sum of all integers divisible by either -66 or -32
    for i in range(start_index, end_index + 1):
        if my_list[i] % (-66) == 0 or my_list[i] % (-32) == 0:
            sum += my_list[i]
    # Return the sum
    return sum
