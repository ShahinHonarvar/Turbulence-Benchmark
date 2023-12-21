
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    lower_bound = 40
    upper_bound = 200
    # Iterate through the list and calculate the sum of all integers divisible by either 21 or 71
    for i in range(lower_bound, upper_bound + 1):
        if my_list[i] % 21 == 0 or my_list[i] % 71 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
