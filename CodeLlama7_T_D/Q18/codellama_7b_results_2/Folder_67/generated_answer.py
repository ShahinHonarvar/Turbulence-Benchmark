
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the specified range of the input list
    for i in range(24, 32 + 1):
        # Check if the current element is divisible by either 35 or 87
        if my_list[i] % 35 == 0 or my_list[i] % 87 == 0:
            # If it is, add it to the total sum
            total += my_list[i]

    # Return the total sum
    return total
