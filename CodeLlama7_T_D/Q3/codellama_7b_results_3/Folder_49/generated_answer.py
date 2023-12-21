
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the input list and append each positive integer to the output list
    for i in range(80, 201):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # Return the output list of positive integers
    return pos_ints
