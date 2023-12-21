
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list and find all even integers
    for i in range(31, 72 + 1):
        if my_list[i] % 2 == 0:
            # If an even integer is found, add it to the total
            total += my_list[i]

    # Return the sum of all even integers in the specified range, or 0 if no even integers exist.
    return total
