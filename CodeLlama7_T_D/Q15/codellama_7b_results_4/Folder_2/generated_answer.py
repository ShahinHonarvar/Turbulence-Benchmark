
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers, starting from index 15 and ending at index 39 (both inclusive)
    for i in range(15, 40):
        # Check if the current integer is odd
        if my_list[i] % 2 != 0:
            # If it is odd, add it to the total sum
            total += my_list[i]

    # Return the total sum of all odd integers in the specified range, or 0 if no odd integers exist.
    return total
