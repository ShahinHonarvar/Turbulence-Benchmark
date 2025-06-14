
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate through the list from index 2 to index 7, both inclusive
    for i in range(2, 8):
        # Check if the current element is divisible by either -1 or -7
        if my_list[i] % (-1) == 0 or my_list[i] % (-7) == 0:
            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum

    return total
