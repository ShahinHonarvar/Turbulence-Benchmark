
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list of integers
    for i in range(5):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current element to the sum
            total += my_list[i]
    # Return the sum
    return total
