
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list and append any positive integers to the 'pos_ints' list
    for i in range(15, 40):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
