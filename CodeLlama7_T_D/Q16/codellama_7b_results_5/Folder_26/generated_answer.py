
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list from index 62 to index 99 (both inclusive)
    for i in range(62, 100):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the sum
            total += my_list[i]

    # Return the sum of all even integers from index 62 to index 99 (both inclusive), or 0 if no even integers exist in that range.
    return total
