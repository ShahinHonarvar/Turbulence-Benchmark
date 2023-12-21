
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate over the list of integers
    for i in range(527, 539):
        # Check if the current index is odd
        if my_list[i] % 2 != 0:
            # Add the current integer to the sum
            total += my_list[i]
    return total
