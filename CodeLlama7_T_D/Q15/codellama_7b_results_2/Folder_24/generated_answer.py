
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list, starting from index 74 and ending at index 95 (both inclusive)
    for i in range(74, 96):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the total
            total += my_list[i]

    # Return the sum of all odd integers in the specified range, or 0 if no such integers exist
    return total
