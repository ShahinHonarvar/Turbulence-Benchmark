
def all_pos_ints_inclusive(my_list):
    # Create a new list to store the positive integers
    pos_ints = []
    # Loop through the input list and append any positive integers to the output list
    for i in range(40, 201):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
