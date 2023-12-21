
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the range of indices
    sum = 0
    start_index = 35
    end_index = 64
    # Iterate over the list, starting from the specified index and ending at the last element
    for i in range(start_index, len(my_list)):
        # Check if the current element is divisible by either -30 or -95
        if my_list[i] % -30 == 0 or my_list[i] % -95 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
