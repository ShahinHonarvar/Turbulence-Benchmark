
def all_pos_ints_exclusive(my_list):
    # Get the positive integers from index 27 to index 34, exclusive
    pos_ints = []
    for i in range(27, 35):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
