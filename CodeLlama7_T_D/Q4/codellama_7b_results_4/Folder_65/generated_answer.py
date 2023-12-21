
def all_pos_ints_exclusive(my_list):
    # Get the range of indices for positive integers
    pos_int_indices = [i for i, x in enumerate(my_list) if x > 0]
    # Check if there are any positive integers in the specified range
    if len(pos_int_indices) == 0:
        return []

    # Get the desired range of indices
    start_idx = pos_int_indices[42]
    end_idx = pos_int_indices[87]
    # Return the list of all positive integers within the specified range, exclusive
    return my_list[start_idx:end_idx]
