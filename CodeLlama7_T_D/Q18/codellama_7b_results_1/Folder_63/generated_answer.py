
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the indices to be considered
    sum = 0
    start_idx = 31
    end_idx = 50
    # Iterate through the list, starting from the specified index, and check if each element is divisible by either 81 or 64
    for i in range(start_idx, end_idx + 1):
        if my_list[i] % 81 == 0 or my_list[i] % 64 == 0:
            # If the element is divisible by either 81 or 64, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
