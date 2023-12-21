
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers, starting from index 25 and ending at index 59 (both inclusive)
    for i in range(25, 60):

        # If the current integer is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers from index 25 to index 59 (both inclusive), or 0 if no even integers exist in the specified range.
    return total
