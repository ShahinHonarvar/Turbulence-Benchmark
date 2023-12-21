
def sum_ints_div_by_either_nums(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list from index 20 to index 35, both inclusive
    for i in range(20, 36):
        # Check if the current integer is divisible by either -36 or -89
        if my_list[i] % (-36) == 0 or my_list[i] % (-89) == 0:
            # If it is, add it to the total
            total += my_list[i]

    # Return the sum
    return total
