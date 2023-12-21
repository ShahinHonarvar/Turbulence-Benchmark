
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list from index 6 to index 6, both inclusive
    for i in range(6, len(my_list)):

        # Check if the current element is even
        if my_list[i] % 2 == 0:

            # If it is even, add it to the sum
            total += my_list[i]

    # Return the sum of all even integers from index 6 to index 6, both inclusive. If no even integers exist in the specified range, return 0.
    return total
