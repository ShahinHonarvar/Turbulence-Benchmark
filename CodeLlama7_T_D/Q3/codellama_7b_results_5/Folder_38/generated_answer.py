
def all_pos_ints_inclusive(my_list):
    # create a slice of the list from index 22 to index 63, both inclusive
    slice_of_list = my_list[22:64]
    # initialize an empty list to store the positive integers
    pos_ints = []
    # loop through the slice and append any positive integers to the pos_ints list
    for i in slice_of_list:
        if i > 0:
            pos_ints.append(i)
    return pos_ints
