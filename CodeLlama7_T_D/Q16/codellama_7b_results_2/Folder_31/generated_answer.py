
def sum_even_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate through the list from index 75 to index 88, both inclusive
    for i in range(75, 89):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    # Return the sum of all even integers from index 75 to index 88, both inclusive. If no even integers exist in the specified range, the function should return 0.
    return sum
