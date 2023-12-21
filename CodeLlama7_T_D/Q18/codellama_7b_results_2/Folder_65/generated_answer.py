
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 50
    end_index = 92

    # Iterate through the list and check for divisibility by either -94 or -95
    for i in range(start_index, end_index + 1):
        if my_list[i] % -94 == 0 or my_list[i] % -95 == 0:
            sum += my_list[i]

    # Return the sum of all integers divisible by either -94 or -95
    return sum
