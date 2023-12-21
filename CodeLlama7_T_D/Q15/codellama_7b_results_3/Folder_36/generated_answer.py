
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate over the list from index 246 to index 750, both inclusive
    for i in range(246, 751):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the sum
            total += my_list[i]
    # Return the sum
    return total
