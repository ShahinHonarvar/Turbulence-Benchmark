
def all_pos_ints_exclusive(my_list):
    # Get the indices of the first and last positive integers
    first_pos_int = next((i for i, x in enumerate(my_list) if x > 0)), None
    last_pos_int = next((i for i, x in enumerate(reversed(my_list))) if x > 0), None
    # Get the range of positive integers between the first and last indices
    pos_ints_range = range(first_pos_int + 1, last_pos_int)
    # Return the list of all positive integers in the specified range
    return [my_list[i] for i in pos_ints_range]
