
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate over the list from index 31 to index 34, both inclusive
    for i in range(31, 35):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the total
            total += my_list[i]
    # Return the sum of all even integers in the specified range, or 0 if no such integers exist.
    return total
