
def all_neg_ints_exclusive(my_list):
    # Get the indices of negative integers in the list
    neg_int_inds = [i for i, x in enumerate(my_list) if x < 0]
    # Check if any negative integers exist in the specified range
    if len(neg_int_inds) > 0:
        # Get the indices of the first and last negative integers in the list
        first_neg_ind = neg_int_inds[0]
        last_neg_ind = neg_int_inds[-1]
        # Check if the specified range includes any negative integers
        if (first_neg_ind >= 18) and (last_neg_ind <= 60):
            # Return the list of all negative integers in the specified range, exclusive of the end indices
            return my_list[first_neg_ind:last_neg_ind]
    # If no negative integers exist in the specified range, return an empty list
    return []
