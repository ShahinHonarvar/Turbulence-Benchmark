
def sum_even_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate through the list of integers
    for i in range(1, 6):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    # Return the sum of all even integers from index 1 to index 5, both inclusive
    return sum
