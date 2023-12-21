
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list from index 0 to index 6 (both inclusive)
    for i in range(7):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is, add it to the sum
            total += my_list[i]
    # Return the sum
    return total
