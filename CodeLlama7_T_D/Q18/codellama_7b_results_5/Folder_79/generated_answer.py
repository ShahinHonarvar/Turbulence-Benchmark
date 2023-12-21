
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the list from index 8 to index 9, both inclusive
    for i in range(8, 10):

        # Check if the current element is divisible by either -3 or 6
        if my_list[i] % (-3) == 0 or my_list[i] % 6 == 0:

            # Add the current element to the sum
            total += my_list[i]

    # Return the sum
    return total
