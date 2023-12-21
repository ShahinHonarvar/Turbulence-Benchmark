
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Iterate through the input list from index 14 to index 64, both inclusive
    for i in range(14, 65):

        # Check if the current element is a positive integer and add it to the list of positive integers
        if my_list[i] > 0:
            pos_ints.append(my_list[i])

    # Return the list of all positive integers from index 14 to index 64, both inclusive
    return pos_ints
