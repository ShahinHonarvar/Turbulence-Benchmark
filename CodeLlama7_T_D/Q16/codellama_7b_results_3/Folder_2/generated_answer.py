
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting from index 15 and ending at index 39 (both inclusive)
    for i in range(15, 40):

        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:

            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum of all even integers from index 15 to index 39 (both inclusive), or 0 if no even integers exist in the specified range.
    return total
