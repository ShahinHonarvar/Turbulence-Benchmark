
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 80
    end_index = 200
    # Iterate over the list and add up the divisible integers
    for i in range(start_index, end_index + 1):
        if my_list[i] % 10 == 0 or my_list[i] % 1000 == 0:
            total += my_list[i]
    return total
