
def all_neg_ints_exclusive(my_list):
    # Get the range of indices for negative integers
    neg_int_range = [i for i in range(50, 201) if my_list[i] < 0]
    # Return an empty list if no negative integers exist in the specified range
    if not neg_int_range:
        return []

    # Return the list of all negative integers from index 50 to index 200, both exclusive
    return [my_list[i] for i in neg_int_range]
