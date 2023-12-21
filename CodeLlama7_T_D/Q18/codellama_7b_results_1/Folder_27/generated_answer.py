
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate through the list of integers
    for i in range(20, 36 + 1):

        # Check if the current integer is divisible by either -36 or -89
        if my_list[i] % -36 == 0 or my_list[i] % -89 == 0:

            # If it is, add it to the total
            total += my_list[i]

    # Return the sum
    return total
