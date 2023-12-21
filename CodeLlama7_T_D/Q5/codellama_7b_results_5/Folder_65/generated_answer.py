
def all_neg_ints_inclusive(my_list):
    # Get the indices of negative integers in the list
    neg_int_indices = [i for i, x in enumerate(my_list) if x < 0]
    # Check if any negative integers exist in the specified range
    if len(neg_int_indices) == 0:
        return []

    # Return the list of all negative integers from index 56 to index 98, both inclusive
    return [my_list[i] for i in neg_int_indices if 56 <= i <= 98]
