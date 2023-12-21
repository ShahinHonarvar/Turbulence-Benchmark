
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list from index 25 to index 87, both inclusive
    for i in range(25, 88):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # Add the current element to the sum
            total += my_list[i]
    # Return the sum of all even integers in the specified range, or 0 if no such integers exist
    return total
