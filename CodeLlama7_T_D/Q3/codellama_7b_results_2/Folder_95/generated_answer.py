
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(82, 86 + 1):

        # Check if the current element is a positive integer
        if my_list[i] > 0:

            # If it is, add it to the list of positive integers
            pos_ints.append(my_list[i])

    # Return the list of all positive integers from index 82 to index 86, both inclusive
    return pos_ints
