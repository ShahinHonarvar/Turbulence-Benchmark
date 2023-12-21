
def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through the list from index 64 to 66, inclusive
    for i in range(64, 67):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
