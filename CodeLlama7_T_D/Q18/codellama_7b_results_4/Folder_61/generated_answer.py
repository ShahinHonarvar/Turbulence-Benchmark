
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the list of integers
    for i in range(len(my_list)):

        # Check if the current integer is divisible by either -5 or -6
        if my_list[i] % -5 == 0 or my_list[i] % -6 == 0:

            # Add the current integer to the sum
            total += my_list[i]

    # Return the sum of all integers divisible by either -5 or -6 from index 0 to index 6, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
