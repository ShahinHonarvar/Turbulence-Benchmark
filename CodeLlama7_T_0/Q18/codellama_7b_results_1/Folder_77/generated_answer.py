
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 828
    end_index = 932
    # Iterate through the list and calculate the sum of all integers divisible by either -649 or -461
    for i in range(start_index, end_index + 1):
        if my_list[i] % -649 == 0 or my_list[i] % -461 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
