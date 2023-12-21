
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list and check for positive integers in the specified range
    for i in range(56, 88 + 1):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
