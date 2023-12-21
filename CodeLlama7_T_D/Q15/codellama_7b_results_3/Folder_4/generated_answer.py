
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list from index 12 to index 92, both inclusive
    for i in range(12, 93):
        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            total += my_list[i]
    # Return the sum of all odd integers from index 12 to index 92, both inclusive. If no odd integers exist in the specified range, the function should return 0.
    return total
