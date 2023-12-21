
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list from index 686 to index 987, both inclusive
    for i in range(686, 988):

        # Check if the current element is even
        if my_list[i] % 2 == 0:

            # Add the current element to the sum
            total += my_list[i]

    # Return the sum of all even integers from index 686 to index 987, both inclusive. If no even integers exist in the specified range, the function should return 0.
    return total
