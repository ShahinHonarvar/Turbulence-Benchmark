
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the indices
    total = 0
    start_index = 58
    end_index = 81
    # Iterate over the list, starting from the specified index
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 55 or 10
        if my_list[i] % 55 == 0 or my_list[i] % 10 == 0:
            # If it is, add it to the total sum
            total += my_list[i]
    # Return the total sum
    return total
