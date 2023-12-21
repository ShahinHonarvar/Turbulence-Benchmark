
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    lower_bound = 30
    upper_bound = 200
    # Loop through the list and find all integers divisible by either -115 or 115
    for i in range(lower_bound, upper_bound + 1):
        if my_list[i] % -115 == 0 or my_list[i] % 115 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either -115 or 115 from index 30 to index 200, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
