
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the list from index 73 to index 86, inclusive
    for i in range(73, 87):

        # Check if the current integer is divisible by either 54 or 82
        if my_list[i] % 54 == 0 or my_list[i] % 82 == 0:

            # If it is, add it to the total
            total += my_list[i]

    # Return the total sum of all integers divisible by either 54 or 82 from index 73 to index 86, inclusive. If no such integers exist in the specified range, return 0.
    return total
