
def all_neg_ints_inclusive(my_list):
    # Get the indices of negative integers in the list
    neg_inds = [i for i, x in enumerate(my_list) if x < 0]
    # Check if there are any negative integers in the specified range
    if len(neg_inds) > 0 and (neg_inds[0] >= 35 and neg_inds[-1] <= 49):
        # Return the list of all negative integers from index 35 to index 49, both inclusive
        return [my_list[i] for i in range(35, 50)]
    else:
        # No negative integers exist in the specified range, so return an empty list
        return []
