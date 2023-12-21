
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 22
    end_index = 24
    # Iterate through the list and calculate the sum of all integers divisible by either -85 or -30
    for i in range(start_index, end_index + 1):
        if my_list[i] % -85 == 0 or my_list[i] % -30 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
