
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list from index 28 to index 40, both inclusive
    for i in range(28, 41):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum of all odd integers in the specified range, or 0 if no such integers exist
    return total
