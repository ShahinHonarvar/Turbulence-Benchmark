
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Iterate over the input list and append any positive integers to the output list
    for i in range(len(my_list)):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])

    # Return the list of all positive integers from index 0 to index 8, both exclusive
    return pos_ints
