
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 48
    end_index = 76
    # Loop through the list and check if each integer is divisible by either -46 or -82
    for i in range(start_index, end_index + 1):
        if my_list[i] % -46 == 0 or my_list[i] % -82 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either -46 or -82 from index 48 to index 76, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
