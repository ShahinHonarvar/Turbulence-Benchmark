
def all_neg_ints_inclusive(my_list):
    # Get the indices of negative integers in the specified range
    neg_int_indices = [i for i, x in enumerate(my_list[33:37]) if x < 0]
    # Return the list of all negative integers from index 33 to index 36, both inclusive
    return [my_list[i] for i in neg_int_indices]
