
def sum_even_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through the list from index 0 to index 3, both inclusive
    for i in range(4):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
