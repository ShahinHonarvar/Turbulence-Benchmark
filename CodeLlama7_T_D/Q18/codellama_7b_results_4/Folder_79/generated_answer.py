
def sum_ints_div_by_either_nums(my_list):
    # initialize variables
    total = 0
    start_index = 8
    end_index = 9

    # loop through the list and calculate the sum of all integers divisible by either -3 or 6 from index 8 to index 9, both inclusive
    for i in range(start_index, end_index + 1):
        if my_list[i] % (-3) == 0 or my_list[i] % 6 == 0:
            total += my_list[i]

    # return the sum of all integers divisible by either -3 or 6 from index 8 to index 9, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
