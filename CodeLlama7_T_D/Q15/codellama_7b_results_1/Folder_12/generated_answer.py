
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate through the list from index 14 to index 64, both inclusive
    for i in range(14, 65):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
