
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list from index 30 to index 87, both inclusive
    for i in range(30, 88):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current element to the sum
            sum += my_list[i]
    # Return the sum of all odd integers in the specified range, or 0 if no odd integers exist
    return sum
