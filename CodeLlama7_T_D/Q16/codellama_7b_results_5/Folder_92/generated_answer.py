
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list of integers from index 0 to index 1, both inclusive
    for i in range(2):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum of all even integers from index 0 to index 1, both inclusive. If no even integers exist in the specified range, return 0.
    return sum
