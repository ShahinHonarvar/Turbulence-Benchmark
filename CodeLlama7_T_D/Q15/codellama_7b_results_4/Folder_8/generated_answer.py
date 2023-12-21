
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list from index 23 to index 23, both inclusive
    for i in range(23, 24):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # Add the current element to the total sum
            total += my_list[i]

    # Return the total sum
    return total
