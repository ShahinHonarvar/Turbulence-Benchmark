
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting from index 29 and ending at index 79 (both inclusive)
    for i in range(29, 80):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers from index 29 to index 79 (both inclusive), or 0 if no even integers exist in the specified range.
    return total
