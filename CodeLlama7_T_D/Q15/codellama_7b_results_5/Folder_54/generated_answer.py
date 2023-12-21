
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list, starting from index 34 and ending at index 55 (inclusive)
    for i in range(34, 56):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the sum
            total += my_list[i]
    # Return the sum
    return total
