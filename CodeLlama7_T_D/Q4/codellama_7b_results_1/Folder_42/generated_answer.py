
def all_pos_ints_exclusive(my_list):
    # Create a slice of the input list from index 44 to index 67, both exclusive
    slice_ = my_list[44:67]
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the slice and append any positive integers to the pos_ints list
    for i in slice_:
        if i > 0:
            pos_ints.append(i)
    # Return the pos_ints list
    return pos_ints
