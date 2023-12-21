
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate through the list starting from index 10
    for i in range(10, len(my_list)):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    # Return the sum of all even integers from index 10 to index 100, both inclusive. If no even integers exist in the specified range, return 0.
    return sum
