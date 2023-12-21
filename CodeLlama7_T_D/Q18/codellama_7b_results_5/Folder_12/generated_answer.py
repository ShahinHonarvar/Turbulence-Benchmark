
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate through the list of integers from index 35 to index 64, both inclusive
    for i in range(35, 65):
        # Check if the current integer is divisible by either -30 or -95
        if my_list[i] % (-30) == 0 or my_list[i] % (-95) == 0:
            # If it is, add it to the sum
            total += my_list[i]
    # Return the sum of all integers divisible by either -30 or -95 from index 35 to index 64, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
