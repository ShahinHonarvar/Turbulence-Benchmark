
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list from index 34 to index 55, both inclusive
    for i in range(34, 56):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # Add the current element to the total sum
            total += my_list[i]

    # Return the total sum
    return total
