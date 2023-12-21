
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 11
    end_index = 46
    # Iterate through the list and calculate the sum of all integers divisible by either 55 or 36
    for i in range(start_index, end_index + 1):
        if my_list[i] % 55 == 0 or my_list[i] % 36 == 0:
            sum += my_list[i]
    return sum
