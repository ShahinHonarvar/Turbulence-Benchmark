
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 41
    end_index = 56
    # Iterate through the list and calculate the sum of all integers divisible by either 82 or 90
    for i in range(start_index, end_index + 1):
        if my_list[i] % 82 == 0 or my_list[i] % 90 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
