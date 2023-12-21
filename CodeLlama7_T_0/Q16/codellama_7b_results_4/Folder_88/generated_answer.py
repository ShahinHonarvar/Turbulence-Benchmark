
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers, starting from index 4 and ending at index 8 (both inclusive)
    for i in range(4, 9):

        # If the current element is even, add it to the total
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers from index 4 to index 8 (both inclusive), or 0 if no even integers exist in the specified range.
    return total
