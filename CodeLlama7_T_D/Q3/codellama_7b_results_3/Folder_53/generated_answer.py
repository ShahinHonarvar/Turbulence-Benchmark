
def all_pos_ints_inclusive(my_list):
    # Define a range of indices
    indices = range(100, 201)
    # Filter the list for positive integers
    pos_ints = [x for x in my_list if isinstance(x, int) and x > 0]
    # Return the subset of positive integers within the specified range
    return [pos_ints[i] for i in indices if i < len(pos_ints)]
