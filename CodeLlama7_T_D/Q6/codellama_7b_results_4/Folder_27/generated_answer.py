
def all_neg_ints_exclusive(my_list):
    # Get the indices of the negative integers in the specified range
    neg_int_indices = [i for i, x in enumerate(my_list) if x < 0]
    # Check if any negative integers exist in the specified range
    if len(neg_int_indices) == 0:
        # If no negative integers exist, return an empty list
        return []

    # Get the indices of the first and last negative integers in the specified range
    first_neg_int_index = neg_int_indices[0]
    last_neg_int_index = neg_int_indices[-1]

    # Check if the specified range includes only one negative integer
    if first_neg_int_index == last_neg_int_index:
        # If the specified range includes only one negative integer, return a list containing that integer
        return [my_list[first_neg_int_index]]

    # Get the indices of the negative integers in the specified range, excluding the first and last negative integers
    neg_int_indices = neg_int_indices[1:-1]

    # Return a list containing the negative integers from the specified range, excluding the first and last negative integers
    return [my_list[i] for i in neg_int_indices]
