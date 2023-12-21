
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the list from index 82 to index 86, both inclusive
    for i in range(82, 87):

        # If the current element is even, add it to the total
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers from index 82 to index 86, both inclusive. If no even integers exist in the specified range, return 0.
    return total
