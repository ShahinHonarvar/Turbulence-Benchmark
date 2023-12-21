
def all_pos_ints_inclusive(my_list):
    # Get the range of positive integers in the list
    pos_int_range = range(20, 201)
    # Filter the list to get only the positive integers within the range
    filtered_list = [x for x in my_list if x in pos_int_range]
    return filtered_list
