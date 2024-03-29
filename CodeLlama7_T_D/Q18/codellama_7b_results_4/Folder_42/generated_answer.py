
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 29
    end_index = 45
    # Loop through the list and find all integers divisible by either 27 or 81 from index 29 to index 45, both inclusive. If no such integers exist in the specified range, the function should return 0.
    for i in range(start_index, end_index + 1):
        if my_list[i] % 27 == 0 or my_list[i] % 81 == 0:
            sum += my_list[i]
    return sum
