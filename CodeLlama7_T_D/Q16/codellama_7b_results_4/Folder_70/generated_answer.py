
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate over the list, starting from index 28
    for i in range(28, len(my_list)):

        # Check if the current element is even
        if my_list[i] % 2 == 0:

            # Add the current element to the sum
            total += my_list[i]

    # Return the sum of all even integers in the specified range, or 0 if no even integers exist.
    return total
