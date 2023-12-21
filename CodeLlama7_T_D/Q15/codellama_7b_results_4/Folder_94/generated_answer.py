
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the list from index 28 to 40 (both inclusive)
    for i in range(28, 41):
        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the sum of all odd integers from index 28 to index 40 (both inclusive), or 0 if no such integers exist.
    return total
