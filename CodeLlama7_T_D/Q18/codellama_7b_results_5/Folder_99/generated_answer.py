
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 154
    end_index = 798
    # Iterate through the list and add up the divisible integers
    for i in range(start_index, end_index + 1):
        if my_list[i] % 275 == 0 or my_list[i] % 580 == 0:
            sum += my_list[i]
    return sum
