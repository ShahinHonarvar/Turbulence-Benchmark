
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 20
    end_index = 93
    # Iterate through the list and calculate the sum of all integers divisible by either -92 or -50
    for i in range(start_index, end_index + 1):
        if my_list[i] % -92 == 0 or my_list[i] % -50 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
