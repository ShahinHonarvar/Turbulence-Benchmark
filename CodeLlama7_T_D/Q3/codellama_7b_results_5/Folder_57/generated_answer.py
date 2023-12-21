
def all_pos_ints_inclusive(my_list):
    # Create a new list to store the positive integers
    pos_ints = []
    # Iterate through the list and append any positive integers to the new list
    for i in range(27, 56):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # Return the new list of positive integers
    return pos_ints
