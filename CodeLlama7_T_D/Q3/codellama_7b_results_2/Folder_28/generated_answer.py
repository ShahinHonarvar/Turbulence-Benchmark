
def all_pos_ints_inclusive(my_list):
    # Get the range of indices for positive integers
    pos_int_indices = [i for i, x in enumerate(my_list) if x > 0]
    # Check if any positive integers exist in the specified range
    if not pos_int_indices:
        return []

    # Get the indices of the first and last positive integers
    first_pos_int = min(pos_int_indices)
    last_pos_int = max(pos_int_indices)
    # Return the list of all positive integers within the specified range
    return [my_list[i] for i in range(first_pos_int, last_pos_int + 1)]
