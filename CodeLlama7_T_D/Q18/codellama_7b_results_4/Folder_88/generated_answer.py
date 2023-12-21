
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    lower_bound = 3
    upper_bound = 9

    # Iterate through the list and calculate the sum of all integers divisible by either 6 or 1 within the specified range
    for i in range(lower_bound, upper_bound + 1):
        if my_list[i] % 6 == 0 or my_list[i] % 1 == 0:
            sum += my_list[i]

    # Return the sum of all integers divisible by either 6 or 1 within the specified range
    return sum
