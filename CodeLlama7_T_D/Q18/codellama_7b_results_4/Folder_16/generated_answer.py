
def sum_ints_div_by_either_nums(my_list):
    # initialize variables
    start_index = 55
    end_index = 80
    total_sum = 0

    # loop through the list and calculate the sum of all integers divisible by either 22 or 32
    for i in range(start_index, end_index + 1):
        if my_list[i] % 22 == 0 or my_list[i] % 32 == 0:
            total_sum += my_list[i]

    # return the sum of all integers divisible by either 22 or 32 from index 55 to index 80, both inclusive
    return total_sum
