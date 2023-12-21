
def all_pos_ints_exclusive(my_list):
    # Get the range of positive integers in the list
    pos_int_range = range(20, 36)
    # Filter the list to get only the positive integers in the specified range
    pos_ints = list(filter(lambda x: x in pos_int_range, my_list)))
    return pos_ints
