
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 828
    end_index = 932
    # Iterate through the list in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either -649 or -461
        if my_list[i] % -649 == 0 or my_list[i] % -461 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
