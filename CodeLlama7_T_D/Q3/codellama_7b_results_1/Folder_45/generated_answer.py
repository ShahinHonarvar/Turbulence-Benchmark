
def all_pos_ints_inclusive(my_list):
    # Create a new list to store the positive integers
    pos_ints = []
    # Iterate through the list and append each positive integer to the new list
    for i in range(30, 201):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
