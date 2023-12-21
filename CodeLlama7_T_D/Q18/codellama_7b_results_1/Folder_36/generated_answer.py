
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 299
    end_index = 382
    # Iterate through the list and calculate the sum of all integers divisible by either 858 or 952
    for i in range(start_index, end_index + 1):
        if my_list[i] % 858 == 0 or my_list[i] % 952 == 0:
            total += my_list[i]
    return total
