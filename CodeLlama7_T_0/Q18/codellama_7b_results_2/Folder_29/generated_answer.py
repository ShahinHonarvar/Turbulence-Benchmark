
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 55
    end_index = 84
    # Iterate through the list and calculate the sum of all integers divisible by either -24 or -11
    for i in range(start_index, end_index + 1):
        if my_list[i] % -24 == 0 or my_list[i] % -11 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
