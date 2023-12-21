
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the list of integers from index 10 to index 79, both inclusive
    for i in range(10, 80):

        # Check if the current integer is divisible by either -74 or -58
        if my_list[i] % (-74) == 0 or my_list[i] % (-58) == 0:

            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum
    return total
