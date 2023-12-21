
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate through the list from index 56 to index 98, inclusive
    for i in range(56, 99 + 1):
        # If the current element is even
        if my_list[i] % 2 == 0:
            # Add it to the sum
            total += my_list[i]
    # Return the sum
    return total
