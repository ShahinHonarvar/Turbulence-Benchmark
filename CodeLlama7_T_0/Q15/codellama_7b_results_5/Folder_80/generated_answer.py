
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers
    for i in range(64, 67):
        # Check if the current index is odd
        if my_list[i] % 2 != 0:
            # Add the current integer to the sum
            total += my_list[i]

    # Return the sum of all odd integers in the specified range, or 0 if no odd integers exist
    return total
