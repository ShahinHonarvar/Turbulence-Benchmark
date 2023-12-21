
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list from index 35 to index 49, both inclusive
    for i in range(35, 50):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # Add the current element to the sum
            total += my_list[i]

    # Return the sum of all odd integers from index 35 to index 49, both inclusive. If no odd integers exist in the specified range, return 0.
    return total
