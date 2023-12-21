
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list from index 4 to index 4, both inclusive
    for i in range(4, 5):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # Add the current element to the sum
            total += my_list[i]

    # Return the sum of all odd integers from index 4 to index 4, both inclusive
    return total
