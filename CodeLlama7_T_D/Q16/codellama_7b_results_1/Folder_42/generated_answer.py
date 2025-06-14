
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list, starting from index 29 and ending at index 79 (both inclusive)
    for i in range(29, 80):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum of all even integers in the specified range, or 0 if no even integers exist
    return total
