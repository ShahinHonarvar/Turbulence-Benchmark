
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers, starting from index 10 and ending at index 66
    for i in range(10, 66 + 1):

        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the sum of all odd integers in the specified range, or 0 if no odd integers exist
    return total
