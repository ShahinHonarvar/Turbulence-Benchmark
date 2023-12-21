
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate through the list of integers
    for i in range(8, 10):
        # Check if the current integer is even
        if my_list[i] % 2 == 0:
            # Add the even integer to the sum
            total += my_list[i]
    # Return the sum of all even integers in the specified range
    return total
