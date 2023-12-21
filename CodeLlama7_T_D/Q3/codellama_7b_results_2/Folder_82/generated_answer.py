
def all_pos_ints_inclusive(my_list):
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return []

    # Initialize an empty list to store the positive integers

    pos_ints = []

    # Loop through the list and append any positive integers to the pos_ints list

    for i in range(20, 201):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])

    return pos_ints
