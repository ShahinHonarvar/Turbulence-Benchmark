
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting from index 262 and ending at index 746
    for i in range(262, 747):

        # If the current element is even, add it to the total
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers in the specified range, or 0 if no even integers exist
    return total
