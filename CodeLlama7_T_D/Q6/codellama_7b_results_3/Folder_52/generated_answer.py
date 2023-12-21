
def all_neg_ints_exclusive(my_list):
    # Get the indices of negative integers in the specified range
    neg_int_indices = [i for i, x in enumerate(my_list) if x < 0]
    # Check if any negative integers exist in the specified range
    if len(neg_int_indices) == 0:
        return []

    # Get the list of all negative integers from index 93 to index 94, both exclusive
    neg_ints = my_list[neg_int_indices[92]:neg_int_indices[93]]
    return neg_ints
