
def sum_even_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through the list, starting at index 62 and ending at index 63
    for i in range(62, 64):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    # Return the sum of all even integers from index 62 to index 63, both inclusive. If no even integers exist in the specified range, return 0.
    return sum
