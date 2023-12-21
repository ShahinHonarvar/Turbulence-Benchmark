
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers, starting from index 22 and ending at index 63
    for i in range(22, 64):

        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the sum of all odd integers in the specified range, or 0 if no such integers exist.
    return total
