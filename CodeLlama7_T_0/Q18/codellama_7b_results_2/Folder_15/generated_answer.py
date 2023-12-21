
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is divisible by either -2 or 3
        if my_list[i] % (-2) == 0 or my_list[i] % 3 == 0:
            # If it is, add it to the total
            total += my_list[i]

    # Return the sum of all integers divisible by either -2 or 3 from index 0 to index 2, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
