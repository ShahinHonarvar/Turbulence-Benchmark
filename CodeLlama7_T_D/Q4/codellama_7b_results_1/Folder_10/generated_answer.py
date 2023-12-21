
def all_pos_ints_exclusive(my_list):
    # Get the indices of the first and last positive integers in the list
    first_pos_int = next((i for i, x in enumerate(my_list) if x > 0)), None)
    last_pos_int = next((i for i, x in enumerate(my_list[::-1]) if x > 0)), None)
    # Get the sublist of positive integers within the specified range
    pos_ints = my_list[first_pos_int:last_pos_int+1]
    return pos_ints
