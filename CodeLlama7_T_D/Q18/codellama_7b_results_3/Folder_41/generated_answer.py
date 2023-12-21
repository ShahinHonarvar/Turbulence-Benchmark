
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate over the list of integers
    for i in range(len(my_list)):

        # Check if the current integer is divisible by either 6 or -3
        if my_list[i] % 6 == 0 or my_list[i] % (-3) == 0:

            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum
    return total
