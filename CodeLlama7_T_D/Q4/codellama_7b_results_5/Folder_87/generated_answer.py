
def all_pos_ints_exclusive(my_list):
    # Create a new list to store the positive integers
    pos_ints = []
    # Iterate through the list and append each positive integer to the new list
    for i in range(32, 100):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
