
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers, starting from index 1 and ending at index 5, inclusive
    for i in range(1, len(my_list)):
        # If the current element is even, add it to the total
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers from index 1 to index 5, inclusive. If no even integers exist in the specified range, return 0.
    return total
