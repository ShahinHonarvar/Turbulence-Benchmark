
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list starting from index 35 to index 49, both inclusive
    for i in range(35, 50):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the sum
            total += my_list[i]
    # Return the sum of all even integers in the specified range
    return total
