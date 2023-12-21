
def all_neg_ints_exclusive(my_list):
    # Get the indices of negative integers in the range 19-94
    neg_int_indices = [i for i, x in enumerate(my_list) if x < 0 and 19 <= i <= 94]
    # Return an empty list if no negative integers exist in the specified range
    if not neg_int_indices:
        return []

    # Return the list of all negative integers from index 19 to index 94, both exclusive
    return [my_list[i] for i in neg_int_indices]
