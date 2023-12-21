
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 20
    end_index = 35
    # Iterate through the list and add up the integers divisible by either -36 or -89
    for i in range(start_index, end_index + 1):
        if my_list[i] % -36 == 0 or my_list[i] % -89 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
