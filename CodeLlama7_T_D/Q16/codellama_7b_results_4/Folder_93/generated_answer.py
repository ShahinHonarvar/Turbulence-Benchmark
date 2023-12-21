
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list from index 75 to index 94, both inclusive
    for i in range(75, 95):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the total
            total += my_list[i]

    # Return the sum of all even integers from index 75 to index 94, both inclusive. If no even integers exist in the specified range, return 0.
    return total
