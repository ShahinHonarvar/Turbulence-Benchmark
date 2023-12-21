 def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate through the list, starting from index 40 and ending at index 80 (both inclusive)
    for i in range(40, 81):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the sum
            total += my_list[i]
    # Return the sum of all odd integers in the specified range, or 0 if no odd integers exist.
    return total
