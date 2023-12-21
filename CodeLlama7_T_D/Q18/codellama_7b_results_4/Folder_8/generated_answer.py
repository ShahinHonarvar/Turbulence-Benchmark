
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the list from index 36 to index 85, both inclusive
    for i in range(36, 86):
        # Check if the current integer is divisible by either -27 or -96
        if my_list[i] % -27 == 0 or my_list[i] % -96 == 0:
            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum
    return total
