
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 46
    end_index = 91
    # Iterate through the list and calculate the sum of all integers divisible by either 67 or 15
    for i in range(start_index, end_index + 1):
        if my_list[i] % 67 == 0 or my_list[i] % 15 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
