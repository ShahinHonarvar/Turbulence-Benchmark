
def all_neg_ints_exclusive(my_list):
    # Get the indices of the first and last negative integers in the list
    first_neg_index = next((i for i, x in enumerate(my_list) if x < 0), None)
    last_neg_index = next((i for i, x in enumerate(my_list[::-1]) if x < 0), None)
    # If no negative integers exist in the list, return an empty list
    if first_neg_index is None or last_neg_index is None:
        return []

    # Get the range of indices that correspond to the specified range of negative integers
    neg_int_indices = range(first_neg_index + 1, last_neg_index)

    # Return the list of all negative integers from index 27 to index 34, both exclusive
    return [my_list[i] for i in neg_int_indices]
